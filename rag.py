from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
def load_documents():
    loader = TextLoader("document.txt")
    documents = loader.load()
    return documents

documents = load_documents()


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

chunks = split_documents(documents)


def create_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store

vector_store=create_vector_store(chunks)



def retrieve_chunks(vector_store, query):
    results = vector_store.similarity_search(query, k=2)
    return results

query =  input("Ask the Query?")
results=retrieve_chunks(vector_store, query)





def create_context(results):
    context = "\n\n".join(
        result.page_content for result in results
    )

    return context

context = create_context(results)


for i, result in enumerate(results, start=1):
    print(f"\nChunk {i}:")
    print(result.page_content)



def create_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    return llm

llm = create_llm()


def generate_answer(llm, context, query):
    prompt = f"""
Answer the question using only the context below.

Context: {context}

Question: {query}
"""

    response = llm.invoke(prompt)

    return response

response = generate_answer(llm, context, query)

print(response.content[0]["text"])