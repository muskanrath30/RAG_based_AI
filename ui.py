# interface.py
from imports import st, generate_response
# context_manager = ContextManager()

def run_interface():
    st.title("Dynamic RAG-based AI System")
    user_input = st.text_input("Ask any question about Muskan:")

    if st.button("Submit"):
        response = generate_response(user_input)
        st.write(response)

    # if st.button("Show Conversation History"):
    #     st.write(context_manager.get_context())

    # if st.button("Clear History"):
    #     context_manager.clear_context()
    #     st.write("Conversation history cleared.")

if __name__ == "__main__":
    run_interface()