import os
import streamlit as st
from google import genai

# Get API key from Streamlit Secrets or .env
api_key = None

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text
