from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_retriever():
    embeddings = HuggingFaceEmbeddings()

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})
    return retriever


if __name__ == "__main__":
    retriever = get_retriever()

    query = input("Enter your question: ")

    docs = retriever.invoke(query)

    print("\n🔍 Retrieved Results:\n")

    for i, doc in enumerate(docs):
        print(f"Result {i+1}:")
        print(doc.page_content)
        print("-" * 40)