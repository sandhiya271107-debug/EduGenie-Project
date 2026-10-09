import os
from google import genai
def explain_concept(concept: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Explain {concept} in simple way for students"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
