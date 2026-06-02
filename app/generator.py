from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def generate_answer(
    question,
    context
):
        prompt = f"""
You are a company policy assistant.

Answer ONLY using the supplied context.

If the answer cannot be found
in the context, say:

"I do not know based on the provided documents."

Question:
{question}

Context:
{context}
"""
        
        response = llm.invoke(
        prompt
    )

        return response.content
        