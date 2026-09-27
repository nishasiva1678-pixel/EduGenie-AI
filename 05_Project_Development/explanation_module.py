import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_topic(topic: str) -> str:

    prompt = f"""
You are EduGenie, an educational assistant.

Explain the following topic to a beginner:

Topic:
{topic}

Use:
1. Simple definition
2. Easy explanation
3. Simple example
4. Key points

Avoid unnecessarily difficult words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while explaining topic: {str(e)}"