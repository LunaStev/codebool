import argparse
from core.generator import generate_code

def main():
    parser = argparse.ArgumentParser(
        description="CodeBool: AI-powered code generator"
    )
    parser.add_argument("prompt", type=str, help="Prompt for code generation")
    parser.add_argument("--lang", type=str, default="python", help="Programming language")
    parser.add_argument("--out", type=str, help="Output file (optional)")

    args = parser.parse_args()

    code = generate_code(args.prompt, args.lang)

    if args.out:
        with open(args.out, "w", encoding="uft-8") as f:
            f.write(code)
        print(f"Code saved to {args.out}")
    else:
        print("Generated Code:\n")
        print(code)

if __name__ == "__main__":
    main()