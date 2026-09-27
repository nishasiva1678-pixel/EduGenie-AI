import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_quiz(topic: str) -> str:

    prompt = f"""
Create a beginner-friendly quiz about:

{topic}

Create exactly 5 multiple-choice questions.

For each question provide:
- question
- four options
- correct_answer

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question here",
    "options": ["A", "B", "C", "D"],
    "correct_answer": "A"
  }}
]
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        quiz = json.loads(text)

        return json.dumps(quiz, indent=2)

    except Exception as e:
        return f"Error while generating quiz: {str(e)}"