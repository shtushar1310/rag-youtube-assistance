from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings  # ✅ updated
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv()

def ingest(youtube_url: str)-> int:
    loader = YoutubeLoader.from_youtube_url(youtube_url)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",  # ✅ same model both files
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")  # ✅ correct param name
    )

    vectorstore = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="./vectorstore"
    )

    print(f"Stored {len(chunks)} chunks from: {youtube_url}")
    return len(chunks)