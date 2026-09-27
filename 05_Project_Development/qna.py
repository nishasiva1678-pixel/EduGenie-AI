import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Give a simple beginner-friendly answer.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while getting answer: {str(e)}"