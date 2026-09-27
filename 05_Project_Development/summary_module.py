import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text: str) -> str:

    prompt = f"""
Summarize the following educational text.

Keep the important information.
Remove unnecessary repetition.
Make the summary easy for a student to study.

Text:
{text}
"""

    try:
        response = client.models.generate_content(
           model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while summarizing: {str(e)}"