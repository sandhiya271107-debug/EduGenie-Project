import os
from google import genai

def summarize_text(text: str):
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "Error: GEMINI_API_KEY not set in Render"
            
        client = genai.Client(api_key=api_key)
        prompt = f"Summarize this text in simple points for a student:\n\n{text}"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"
