from dotenv import load_dotenv
import requests
import os
import time

load_dotenv() 
HUGGINGFACE_API_KEY = os.getenv("LLM_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("Hugging Face API key not found. Make sure it's in the .env file.")

# Using a smaller, faster model
MODEL_NAME = "tiiuae/falcon-7b-instruct"
BASE_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

def query_huggingface_model(input_text, max_retries=5, wait_time=10):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": input_text}

    for attempt in range(max_retries):
        response = requests.post(BASE_URL, headers=headers, json=payload)

        if response.status_code == 503:
            estimated_time = response.json().get("estimated_time", 30)
            print(f"Model is still loading... Estimated time: {estimated_time} seconds.")
            if attempt == 0:
                return f"Model is warming up. Please wait {int(estimated_time)} seconds."
            time.sleep(min(wait_time, estimated_time))  
            continue

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json()}")  
            return f"Error: {response.status_code} - {response.json()}"

        try:
            return response.json()[0]["generated_text"]
        except KeyError:
            return "Error: Unexpected response format from AI model."

    return "Error: The model is taking too long to load. Please try again later."
