import streamlit as st
from rag_agent import qa

st.title("RAG Knowledge Assistant")
query = st.text_input("Ask a question:")

if query:
    answer = qa.run(query)
    st.write("Answer:", answer)
