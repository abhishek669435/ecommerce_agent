import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_documents():
    docs = []
    folder_path = "data/policies"

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        loader = TextLoader(file_path)
        docs.extend(loader.load())

    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    return splitter.split_documents(docs)

def create_vector_db(chunks):
    embeddings = HuggingFaceEmbeddings()

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="db"
    )

    db.persist()
    print("✅ Vector database created successfully!")

if __name__ == "__main__":
    docs = load_documents()
    chunks = split_documents(docs)

    print("Total documents loaded:", len(docs))
    print("Total chunks created:", len(chunks))

    create_vector_db(chunks)