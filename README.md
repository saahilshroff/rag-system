# Retrieval-Augmented Generation (RAG) Knowledge Repository
This project Retrieval-Augmented Generation (RAG) Knowledge Repository combines information retrieval and generative AI to provide accurate, context-aware responses by retrieving relevant data before generating output.

## Demo
![Demo of Knowledge Retrieval-Augmented Generation](assets/demo.gif)

## Features

- **Documentation Scraping:** Automatically scrapes content from base URLs.
- **User-Friendly Interface:** Simplifies the search for relevant documentation, making it accessible and easy to use.
- **Time-Saving:** Reduces development time by quickly delivering the information needed.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

Follow these steps to set up the project locally:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**1. Clone the repository:**
```bash
    git clone https://github.com/saahilshroff/rag-system.git
    cd rag-system
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**2. Create a virtual environment (optional but recommended):**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**3. Install the required dependencies:**
```bash
    pip install streamlit sentence-transformers unstructured libmagic python-magic python-magic-bin langchain 
    pip install -qU langchain-community faiss-cpu 
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

**4. Create OpenAI Key:**

>Go to this link https://openai.com/index/openai-api/

To access the Embeddings and GPT model in the app, you'll need to add some OpenAI credits. For personal use, it doesn't require much—you can start with as little as $5-$10, which should be enough to last 2-3 months depending on your usage.

Sign up and create your **OpenAI API Key**. Copy the api key and store it securely.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**5. Setup environment variables:**
    
Create a 'secret_key.py' file in the same level as the app.py file. Create an 'OPENAI_API_KEY' variable to store your API key
    
secret_key.py
```bash
    OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
```

## Usage
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**1. Launch the application:**
```bash
    streamlit run app.py
```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**2. Input the base URLs:** Enter the base URLs of the documentation you want to scrape. The FAISS vector database will be updated.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**3. Ask questions:** Inquire about specific information related to the documentation. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**4. Receive tailored responses:** Get relevant answers and the source based on your queries.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**5. Receive tailored responses:** Get relevant answers and the source based on your queries.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**6. Repeat:** The FAISS vector database stores all the past input URLS - so you can enjoy retrieving information, without having to worry about finding past URLs.


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments
- [Langchain](https://www.langchain.com/) for the framework to manage the AI pipeline.
- [OpenAI](https://openai.com/) GPT for providing the language model.
- Special thanks to all contributors and users for their support and feedback.
