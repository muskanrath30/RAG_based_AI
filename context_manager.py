# # context_manager.py
# class ContextManager:
#     def __init__(self):
#         self.context = []

#     def add_context(self, question, answer):
#         """Dynamically adds the latest question and its answer to the context."""
#         self.context.append((question, answer))

#     def get_context(self):
#         """Retrieves the context to maintain the flow of conversation."""
#         return "\n".join([f"Q: {q}\nA: {a}" for q, a in self.context])

#     def clear_context(self):
#         """Clears the conversation history when needed."""
#         self.context = []

# if __name__ == "__main__":
#     context_manager = ContextManager()
#     context_manager.add_context("What are Muskan's skills?", "Muskan is skilled in AI, Python, and Data Science.")
#     print(context_manager.get_context())

# context_manager.py
# class ContextManager:
#     def __init__(self):
#         self.context = []
#         self.last_question = None
#         self.last_answer = None

#     def add_context(self, question, answer):
#         """Dynamically adds the latest question and its answer to the context."""
#         self.last_question = question
#         self.last_answer = answer
#         self.context.append((question, answer))

#     def get_context(self):
#         """Retrieves the context to maintain the flow of conversation."""
#         return "\n".join([f"Q: {q}\nA: {a}" for q, a in self.context])

#     def get_last_interaction(self):
#         """Retrieve the last question and answer for follow-up purposes."""
#         if self.last_question and self.last_answer:
#             return f"Q: {self.last_question}\nA: {self.last_answer}"
#         return ""

#     def clear_context(self):
#         """Clears the conversation history when needed."""
#         self.context = []
#         self.last_question = None
#         self.last_answer = None

# if __name__ == "__main__":
#     context_manager = ContextManager()
#     context_manager.add_context("What are Muskan's skills?", "Muskan is skilled in AI, Python, and Data Science.")
#     print(context_manager.get_context())

# context_manager.py
class ContextManager:
    def __init__(self, max_context_length=3):
        self.context = []
        self.max_context_length = max_context_length  # Maximum number of context entries to keep

    def add_context(self, question, answer):
        """Adds the latest question and its answer to the context."""
        # Append the new question and answer as a tuple
        self.context.append((question, answer))

        # Limit the context length to the last few interactions
        if len(self.context) > self.max_context_length:
            self.context.pop(0)  # Remove the oldest context entry to maintain length

    def get_context(self):
        """Retrieves the relevant context to maintain the flow of conversation."""
        # Only include the last few relevant interactions to keep the context concise
        return "\n".join([f"Q: {q}\nA: {a}" for q, a in self.context[-self.max_context_length:]])

    def clear_context(self):
        """Clears the conversation history when needed."""
        self.context = []

if __name__ == "__main__":
    context_manager = ContextManager()
    context_manager.add_context("What are Muskan's skills?", "Muskan is skilled in AI, Python, and Data Science.")
    context_manager.add_context("What projects has Muskan worked on?", "Muskan has worked on various data science projects including predictive modeling.")
    print(context_manager.get_context())