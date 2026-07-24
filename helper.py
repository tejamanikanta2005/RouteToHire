import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"]
)

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini Error:\n\n{str(e)}"