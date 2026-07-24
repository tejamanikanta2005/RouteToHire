import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"]
)

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text