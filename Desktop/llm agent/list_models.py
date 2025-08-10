import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

print("Attempting to list available models...")

try:
    # Configure the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY not found in .env file.")
    else:
        genai.configure(api_key=api_key)

        # List all available models
        print("-" * 30)
        for m in genai.list_models():
            # Check if the model supports the 'generateContent' method needed by the agent
            if 'generateContent' in m.supported_generation_methods:
                print(f"Model Name: {m.name}")
        print("-" * 30)
        print("\nSUCCESS: Listed all models that support 'generateContent'.")
        print("Please use one of the 'Model Name' values from this list in your agent_logic.py file.")

except Exception as e:
    print(f"\nERROR: An error occurred while trying to list models.")
    print(f"Error details: {e}")