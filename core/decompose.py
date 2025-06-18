import openai
import os
import re
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def lang_to_ext(lang: str) -> str:
    return {
        "python": ".py",
        "rust": ".rs",
        "cpp": ".cpp",
        "c++": ".cpp",
        "c": ".c",
        "typescript": ".ts",
        "javascript": ".js",
        "java": ".java",
        "go": ".go",
    }.get(lang.lower(), ".txt")

def decompose_prompt(prompt: str, lang: str = "python") -> list[str]:
    system = (
        f"You are a software architect. Your job is to decompose a programming task into "
        f"a list of source code filenames used in a project written strictly in {lang}. "
        f"Make sure all filenames use proper file extensions for {lang}, like '.rs' for Rust or '.py' for Python."
    )

    user = (
        f"Decompose the following programming task into a list of source code files "
        f"written in {lang}, and explain their roles. "
        f"Again, all filenames should have the correct extension for {lang}.\n\n"
        f"{prompt}"
    )

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        temperature=0.4,
        max_tokens=800
    )

    raw = res["choices"][0]["message"]["content"]

    # 강력한 정규식으로 정확한 파일명만 추출
    ext = lang_to_ext(lang).lstrip(".")
    pattern = re.compile(r"([a-zA-Z0-9_\-\/]+\.%s)" % re.escape(ext))
    matches = re.findall(pattern, raw)

    return list(set(matches))  # 중복 제거