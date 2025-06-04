# CodeBool

**CodeBool** is an open-source AI coding assistant designed to generate, analyze, and refactor code via simple CLI commands. Built with Python, it aims to provide developers with a lightweight yet powerful tool for enhancing productivity, understanding errors, and generating boilerplate code across multiple languages.

> 🚀 Currently under development. Initial version is focused on Python. Future support for Rust and other languages planned.

---

## Features

- ⚙️ **Code generation** – Generate code snippets using natural language prompts
- 🛠️ **Code analysis** – Understand and explain errors in existing source files
- 🔄 **Refactoring** – Reorganize and improve code structure
- 🧪 **Test case generation** – Create basic test cases for functions or scripts
- 🌐 **Multi-language support** – (Planned) Python, C, Rust, Wave, and more
- 💡 **Simple CLI usage** – Easily accessible from your terminal

---

## Getting Started

### Prerequisites

- Python 3.8+
- Hugging Face (for initial language model backend)

### Installation

```bash
git clone https://github.com/LunaStev/codebool.git
cd Codebool
pip install -r requirements.txt
```

### Usage

```bash
python cli.py "Write a function to check for prime numbers" --lang python
```

## Options (planned)

| Option       | Description                                  |
| ------------ | -------------------------------------------- |
| `--lang`     | Select target language (e.g., `python`, `c`) |
| `--out`      | Save output to a file                        |
| `--analyze`  | Analyze an existing source file for issues   |
| `--refactor` | Refactor the given code file                 |
| `--test`     | Generate test cases for the input file       |

---

## Roadmap

- [ ]  Project initialization
- [ ]  Core CLI interface
- [ ]  Code generation module
- [ ]  Code analysis and refactoring
- [ ]  Language support expansion
- [ ]  VSCode extension (optional)
- [ ]  Rust-based local LLM backend (future)

---

## License

CodeBool is licensed under the Mozilla Public License 2.0 (MPL-2.0).

---

## Author

Created by **@LunaStev** – driven by the belief that coding tools should be fast, free, and developer-first.