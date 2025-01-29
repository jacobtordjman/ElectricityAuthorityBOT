from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv() 
GEMINI_API_KEY = os.getenv("LLM_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("API key not found. Make sure it's in the .env file.")


# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def query_gemini_model(input_text):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Using Google Gemini Pro model
        response = model.generate_content(input_text)
        return response.text  # Extract AI-generated response
    except Exception as e:
        print(f"Error: {e}")
        return "Error: Unable to get a response from Google Gemini."