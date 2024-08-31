# retrieval.py
from imports import index_data

def retrieve_data(query):
    db = index_data()
    # Perform retrieval based on the query using similarity search
    results = db.similarity_search(query, k=5)  # Retrieve top 5 relevant documents

    # Extract relevant page content and prioritize based on keywords in metadata
    context = []
    for result in results:
        if "experience" in query.lower() and "experience" in result.metadata.get('source', ''):
            context.append(result.page_content)
        elif "project" in query.lower() and "projects" in result.metadata.get('source', ''):
            context.append(result.page_content)
        elif "education" in query.lower() and "education" in result.metadata.get('source', ''):
            context.append(result.page_content)
    
    # Fallback to general results if no specific context is found
    if not context:
        context = [result.page_content for result in results]

    return "\n".join(context) if context else "No relevant information found."

if __name__ == "__main__":
    pass
