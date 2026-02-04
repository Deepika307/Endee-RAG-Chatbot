import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_answer_with_context(question, retrieved_chunks):

    context = "\n".join([item[1]["metadata"]["text"] for item in retrieved_chunks])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
