'''
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-lite")
def ask_gemini(question):
    response = model.generate_content(question)
    return response.text
'''
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text