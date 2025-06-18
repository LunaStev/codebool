import os
import openai
import traceback
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt: str, lang: str = "python") -> str:
    system_prompt = f"You are a helpful AI coding assistant. Generate clean, idiomatic, and working {lang} code."

    try:
        user_prompt = f"Generate {lang} code for the following task:\n\n{prompt}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.5,
            max_tokens=1000,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error during code generation: {str(e)}"