from langchain.document_loaders import UnstructuredURLLoader
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

folderName = "faiss_index"

def load_data(input_urls):
    loader = UnstructuredURLLoader(urls=input_urls)
    data = loader.load()
    return data

def split_data(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=150, separators = ['\n\n', '\n', '.', ' '])
    docs = text_splitter.split_documents(data)
    return docs
    # len(docs)

def embeddings_vector_store(docs, embeddings):
    faiss_db = FAISS.from_documents(docs, embeddings)
    if os.path.exists(folderName):
        local_index=FAISS.load_local(folderName, embeddings, allow_dangerous_deserialization = True)
        local_index.merge_from(faiss_db)
        local_index.save_local(folderName)
    else:
        faiss_db.save_local(folder_path=folderName)


def QAchain(llm,embeddings, query):
    if not os.path.exists(os.path.join(folderName, "index.faiss")):
        return {"answer": "Please upload data and submit a query.", "sources": []}
    
    docsearch = FAISS.load_local(folderName, embeddings, allow_dangerous_deserialization = True) 
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=docsearch.as_retriever())
    # langchain.debug = True
    result = chain({"question": query}, return_only_outputs=True)
    return result