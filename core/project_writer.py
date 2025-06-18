import os
from .generator import generate_code

def generate_project(prompt: str, lang: str, files: list[str], base_path: str = "output"):
    os.makedirs(base_path, exist_ok=True)

    for filename in files:
        subprompt = f"Write the content of {filename} for this task:\n\n{prompt}"
        code = generate_code(subprompt, lang)
        file_path = os.path.join(base_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"✅ Generated: {file_path}")