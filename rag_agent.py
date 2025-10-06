# Raag
RAAG PROJECT
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader

# Load documents
loader = TextLoader("data/sample_doc.txt")
docs = loader.load()

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)

# Create RAG QA chain
retriever = vector_store.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=retriever
)

# Example query
query = "What is the main idea of the document?"
answer = qa.run(query)
print("Answer:", answer)
