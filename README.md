RAG Application

A beginner-friendly Retrieval-Augmented Generation (RAG) application built using Python, LangChain, Google Gemini, and FAISS.

This project was created as a learning project to understand how a basic RAG pipeline works from document loading to answer generation.

What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that retrieves relevant information from a knowledge source and provides that information to a Large Language Model (LLM) as context before generating an answer.

Instead of asking the LLM to answer using only its existing knowledge, the application first retrieves relevant information from the provided document.

RAG Pipeline

Document
   ↓
Load Document
   ↓
Split into Chunks
   ↓
Create Embeddings
   ↓
Store Vectors in FAISS
   ↓
Retrieve Relevant Chunks
   ↓
Create Context
   ↓
Send Context + Question to Gemini
   ↓
Generate Answer

Technologies Used

Python

LangChain

Google Gemini

Gemini Embeddings

FAISS

python-dotenv

How It Works

The application loads a text document using TextLoader.

The document is split into smaller chunks using RecursiveCharacterTextSplitter.

Each chunk is converted into an embedding using Google's embedding model.

The embeddings and their associated documents are stored in a FAISS vector store.

When the user enters a question, the application performs similarity search to retrieve relevant chunks.

The retrieved chunks are combined into a context.

The context and question are sent to Gemini.

Gemini generates an answer using the provided context.

Example

The sample document contains information about the Indian actor Suriya.

Example question:

What was Suriya's birth name?

Example answer:

Suriya's birth name is Saravanan Sivakumar.

Project Structure

RAG_APPLICATION/
│
├── rag.py
├── document.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env

The .env file contains the Gemini API key and should not be committed to GitHub.

Setup

1. Clone the repository

git clone https://github.com/sneha0222/RAG-Application.git
cd RAG_APPLICATION

2. Create a virtual environment

python -m venv myenv

3. Activate the virtual environment

Windows:

myenv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Create the .env file

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

6. Run the application

python rag.py

Then enter a question when prompted.

Current Limitations

This is a basic RAG implementation created for learning purposes.

It currently works with a text document.

It uses semantic similarity search.

It retrieves the top 2 chunks.

It does not currently include advanced retrieval techniques such as hybrid search or reranking.

The knowledge source is limited to the provided document.

Learning Goals

This project helped me understand the fundamental components of a RAG pipeline:

Document loading

Text splitting

Embeddings

Vector stores

Similarity search

Context creation

LLM prompting

Answer generation

Future Improvements

Possible future improvements include:

PDF document support

Multiple documents

Metadata filtering

Hybrid search

Reranking

Better source attribution

Streamlit interface