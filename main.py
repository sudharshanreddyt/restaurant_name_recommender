import streamlit as st
import langchain_helper as helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American"),
    index = None,
    placeholder = "Select Cuisine"
)



if cuisine:
    # st.write(f"Selected Option : {cuisine}")

    response = helper.get_restauarnt_name_and_items(cuisine)

    restaurant_name = response["restaurant_name"].strip()
    st.header(restaurant_name)

    description = response["description"].strip()
    st.write(description)

    st.write("**Menu Items**")

    menu_items = response["menu_items"].strip().split(",")
    for item in menu_items:
        st.write("-", item)