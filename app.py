# app.py
from retriever import retrieve_relevant_docs
from generator import generate_response

def main():
    query = input("Ask a legal question: ")
    context = retrieve_relevant_docs(query)
    answer = generate_response(query, context)
    print("\nAnswer:\n", answer)

if __name__ == '__main__':
    main()

# retriever.py
from llama_index import VectorStoreIndex, SimpleDirectoryReader

def retrieve_relevant_docs(query):
    documents = SimpleDirectoryReader("legal_docs").load_data()
    index = VectorStoreIndex.from_documents(documents)
    retriever = index.as_retriever()
    return retriever.retrieve(query)

# generator.py
from transformers import pipeline

def generate_response(query, context):
    rag_pipeline = pipeline("text2text-generation", model="facebook/rag-token-base")
    context_text = " ".join([doc.text for doc in context])
    return rag_pipeline(f"question: {query} context: {context_text}")[0]['generated_text']
