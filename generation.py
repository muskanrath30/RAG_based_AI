# generation.py
from imports import openai, retrieve_data

def generate_response(query):
    retrieved_info = retrieve_data(query)

    combined_context = f"{retrieved_info}\nQuestion: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an RAG based AI application that provides context-aware answers about Muskan, her education, work experience, projects and skills based on provided documents like text, pdf files"},
            {"role": "user", "content": combined_context}
        ],
        max_tokens=150,
        temperature=0.7
    )

    answer = response.choices[0].message['content'].strip()

    return answer

if __name__ == "__main__":
    # print(generate_response("What is Muskan's total work experience?"))
    pass
