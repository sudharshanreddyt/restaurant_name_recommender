# 🍽️ Restaurant Name & Menu Generator

A LangChain-powered application that generates creative restaurant names and corresponding menu items using AI. This project uses LangChain Expression Language (LCEL).

## Features

- **AI-Powered Restaurant Names**: Generates unique and fancy restaurant names based on cuisine type
- **Automatic Menu Generation**: Creates a curated list of 10 menu items matching the restaurant concept
- **Restaurant Descriptions**: Generates a description for the restaurant based on the restaurant name and menu items.

## Getting Started

### Prerequisites

- GROQ API key (or compatible LLM API) - I am using Groq APi key in this project.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudharshanreddyt/restaurant_name_recommender.git
   cd restaurant_name_recommender
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

### Run the Main Application

```bash
streamlit run main.py
```

### Example Output
![alt text](/outputs/image.png)