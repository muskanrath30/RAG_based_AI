from imports import st, generate_response

def run_interface():
    st.title("Dynamic RAG-based AI System")
    user_input = st.text_input("Ask any question about Muskan:")

    if st.button("Submit"):
        response = generate_response(user_input)
        st.write(response)

if __name__ == "__main__":
    run_interface()
