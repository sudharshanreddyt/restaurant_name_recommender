from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq")


def get_restauarnt_name_and_items(cuisine):

    """ 
    Chain 1 : Restaurant Chain
    variable : cuisine
    """
    name_template = "Suggest one fancy and unique restaurant name (maximum 3 words) for a restaurant specializing in {cuisine} cuisine. Respond with only the name, nothing else."
    name_template_prompt = PromptTemplate.from_template(name_template)

    name_chain = name_template_prompt | model | StrOutputParser()


    """ 
    Chain 2 : Menu Items
    variable : restaurant_name
    """
    menu_template = "Suggest menu items for {restaurant_name}. Respond with only a comma-separated list of 10 items, no explanations or extra text."
    menu_template_prompt = PromptTemplate.from_template(menu_template)

    menu_chain = menu_template_prompt | model | StrOutputParser()


    description_template = "Write a short and simple 2-sentence description for {restaurant_name} that serves: {menu_items}"
    description_prompt_template = PromptTemplate.from_template(description_template)

    description_chain = description_prompt_template | model | StrOutputParser()

    # Combine two chains with multiple outputs
    composed_chain = ({"restaurant_name" : name_chain} 
                      | RunnablePassthrough.assign(menu_items = menu_chain) 
                      | RunnablePassthrough.assign(description = description_chain))
    print(composed_chain)

    response = composed_chain.invoke({"cuisine" : cuisine})
    print(response)

    return response


if __name__ == "__main__":
    print(get_restauarnt_name_and_items("Italian"))