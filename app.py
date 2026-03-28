import streamlit as st
import sys
sys.path.append(".")

from src.main import get_retriever, generate_answer

st.title("🛒 E-commerce Support Assistant")

query = st.text_input("Enter your question:")

# 👇 BUTTON ADDED (important fix)
if st.button("Get Answer"):

    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("🔍 Searching policies..."):

            retriever = get_retriever()
            docs = retriever.invoke(query)

            # Debug: show retrieved docs
            st.subheader("📄 Retrieved Documents")
            for doc in docs:
                st.write(doc.page_content)

            context = "\n\n".join([doc.page_content for doc in docs])

            with st.spinner("🤖 Generating answer..."):
                answer = generate_answer(query, context, docs)

            st.subheader("🤖 AI Response")
            st.code(answer)