# generation.py
from imports import openai, retrieve_data

def generate_response(query):
    # Retrieve information specific to the current question only
    retrieved_info = retrieve_data(query)

    # Combine only the retrieved information with the current question
    combined_context = f"{retrieved_info}\nQuestion: {query}"

    # Generate a precise response based on retrieved context only
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an RAG based AI application that provides context-aware answers about Muskan, her education, work experience, projects and skills based on provided documents like text, pdf files"},
            {"role": "user", "content": combined_context}
        ],
        max_tokens=150,
        temperature=0.7
    )

    # Extract the answer from the generated response
    answer = response.choices[0].message['content'].strip()

    return answer

if __name__ == "__main__":
    print(generate_response("What is Muskan's total work experience?"))