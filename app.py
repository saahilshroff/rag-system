import streamlit as st
from langchain import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain_helper import embeddings_vector_store, load_data, QAchain, split_data
import os
from secret_key import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
llm = OpenAI(temperature=0.5, max_tokens=1000)
embeddings = OpenAIEmbeddings()

st.set_page_config(page_title="RAG system", page_icon=":mag:")

st.title("Retrieval-Augmented Generation (RAG) Knowledge Repository")
st.text("Store your data by uploading the information link(s) and ask questions to retrieve information from the stored data.")

st.sidebar.title("Upload and store information link(s)")

input_urls= []

if 'url_count' not in st.session_state:
    st.session_state.url_count = 1

for i in range(st.session_state.url_count):
    input_url = st.sidebar.text_input(f"URL {i+1}", key=f"url_{i}")
    if input_url:
        input_urls.append(input_url)

if st.sidebar.button('Add another URL'):
    st.session_state.url_count += 1

main_placeholder = st.empty()
query = st.text_input("Enter your question:")
if query:
    st.empty()
submit_query_button = st.button("Submit")
submit_button = st.sidebar.button('Update database', type='primary')

if submit_button:
    if not input_urls:
        st.sidebar.warning("No URLs entered. Please input at least one URL.", icon="⚠️")
    if input_urls:
        st.sidebar.success("URLs submitted successfully!", icon="✅")
        st.write("Loading data...")
        data = load_data(input_urls)
        st.write("Data Loaded...")
        st.write("Splitting data...")
        docs = split_data(data)
        st.write("Successful data split...")
        st.write("Creating embeddings...")
        vector_index = embeddings_vector_store(docs,embeddings)
        st.write("Embeddings created...")

if submit_query_button:
    if not query:
        st.warning("Please enter a query", icon="⚠️")
    if query:
        st.write("Querying...")
        result = QAchain(llm, embeddings, query)
        st.subheader("Answer:")
        result['answer']
        st.subheader("Source:")
        result['sources']