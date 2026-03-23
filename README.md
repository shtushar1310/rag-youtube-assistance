# YouTube RAG Chatbot

A Retrieval-Augmented Generation (RAG) application built with FastAPI that allows users to ingest YouTube video content and ask questions about it using AI-powered chat.

## Features

- **Content Ingestion**: Upload and process YouTube video transcripts or documents
- **AI-Powered Chat**: Ask questions about ingested content using LangChain and Groq LLM
- **Vector Storage**: Efficient retrieval using ChromaDB vector database
- **FastAPI Backend**: RESTful API for easy integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`

3. Use the following endpoints:
   - `GET /` - Health check
   - `POST /api/v1/ingest` - Ingest YouTube video content
   - `POST /api/v1/chat` - Ask questions about ingested content

4. Access the interactive API documentation at `http://localhost:8000/docs`

## Project Structure

```
├── main.py              # FastAPI application entry point
├── rag_chain.py         # RAG chain implementation
├── chat.py              # Chat functionality
├── ingest.py            # Content ingestion logic
├── routers/             # API route handlers
│   ├── chat.py
│   └── ingest.py
├── vectorstore/         # ChromaDB vector database storage
└── requirements.txt     # Python dependencies
```

## Requirements

- Python 3.8+
- Groq API key (for LLM integration)
- Internet connection for YouTube content access

## Technologies Used

- **FastAPI**: Modern Python web framework
- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for embeddings
- **Groq**: Fast LLM inference
- **PyPDF**: PDF document processing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

![alt text](<Screenshot 2026-03-23 at 15-08-08 YouTube RAG API - Swagger UI.png>)