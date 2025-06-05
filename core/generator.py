import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt: str, lang: str = "python") -> str:
    system_prompt = f"You are a coding assistant. Generate clean and working {lang} code for the given task."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 필요시 gpt-4로 변경 가능
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=1000,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error during code generation: {str(e)}"