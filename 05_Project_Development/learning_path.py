import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_learning_recommendations(topic: str) -> str:

    prompt = f"""
Create a learning path for:

{topic}

Organize it into:

1. Beginner
2. Basic concepts
3. Intermediate
4. Advanced
5. Practice projects

Also suggest useful types of resources such as:
- Documentation
- Tutorials
- Videos
- Books
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while creating learning path: {str(e)}"