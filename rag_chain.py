from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpointEmbeddings  # ✅ updated
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

load_dotenv()

def build_chain():
    print("Building RAG chain...")

    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",  # ✅ same model as ingest.py
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
    )

    vectorstore = Chroma(
        persist_directory="./vectorstore",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatGroq(
        model="groq/compound-mini",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""you are an assistant answering questions about a YouTube video explain the details of the video if you don't know the answer, say no.

Context:
{context}

Question: {question}

Answer:"""
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain