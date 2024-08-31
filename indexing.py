# indexing.py
from imports import ingest_data
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.schema import Document
from tqdm import tqdm

CHROMA_PATH = "new_chroma"
from langchain.embeddings import OpenAIEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

def chunk_text(text, max_length=500):
    words = text.split()
    for i in range(0, len(words), max_length):
        yield " ".join(words[i:i + max_length])

def index_data():
    print("Ingesting data...")
    all_data, education, experience, projects = ingest_data()

    combined_text = f"{all_data}\n{education}\n{experience}\n{projects}"
    chunks = list(chunk_text(combined_text, max_length=500))

    print(f"Total chunks created: {len(chunks)}")

    documents = []
    for chunk in chunks:
        # Add specific metadata based on context
        if "experience" in chunk.lower():
            documents.append(Document(page_content=chunk, metadata={"source": "experience"}))
        elif "project" in chunk.lower():
            documents.append(Document(page_content=chunk, metadata={"source": "projects"}))
        elif "bachelor" in chunk.lower() or "degree" in chunk.lower():
            documents.append(Document(page_content=chunk, metadata={"source": "education"}))
        else:
            documents.append(Document(page_content=chunk, metadata={"source": "general"}))

    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    batch_size = 5
    print("Indexing documents...")

    for i in tqdm(range(0, len(documents), batch_size), desc="Indexing Documents"):
        batch = documents[i:i + batch_size]
        try:
            db.add_texts(
                texts=[doc.page_content for doc in batch],
                metadatas=[doc.metadata for doc in batch]
            )
        except Exception as e:
            print(f"Error indexing batch {i // batch_size + 1}: {e}")

    print("Documents indexed successfully.")
    return db

if __name__ == "__main__":
    index_data()