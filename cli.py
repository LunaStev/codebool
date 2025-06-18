import argparse
from core.generator import generate_code
from core.decompose import decompose_prompt
from core.project_writer import generate_project

def main():
    parser = argparse.ArgumentParser(
        description="CodeBool: AI-powered code generator"
    )
    parser.add_argument("prompt", type=str, help="Prompt for code generation")
    parser.add_argument("--lang", type=str, default="python", help="Programming language")
    parser.add_argument("--out", type=str, help="Output file (optional)")
    parser.add_argument("--decompose", action="store_true", help="Decompose prompt into components")
    parser.add_argument("--project", action="store_true", help="Generate full project files")

    args = parser.parse_args()

    if args.project:
        print("🧠 Decomposing task into project files...")
        files = decompose_prompt(args.prompt)
        print("📁 Files:", files)
        generate_project(args.prompt, args.lang, files)
    elif args.decompose:
        print("🧠 Decomposing prompt...")
        files = decompose_prompt(args.prompt)
        print("📁 Suggested files:")
        for f in files:
            print(" -", f)
    else:
        code = generate_code(args.prompt, args.lang)

        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"Code saved to {args.out}")
        else:
            print("Generated Code:\n")
            print(code)

if __name__ == "__main__":
    main()