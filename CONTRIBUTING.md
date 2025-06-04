# ⚠️Warning⚠️

> **You must fully understand the project's requirements and guidelines to contribute effectively and avoid inconvenience.**

---

# How to Contribute to CodeBool

CodeBool is an open-source project, and contributions from anyone are welcome. However, please follow these guidelines to ensure your contributions align with the project's goals and standards.

---

## Programming Languages

We use **Python** and **Rust** as the primary programming language for developing CodeBool and its core tools.

### Supported Languages

- **[Python](https://www.python.org/)** – Main implementation language
- **[Rust](https://www.rust-lang.org/)** – Planned for full migration after bootstrapping

--- 

## How to Contribute

### Fork the Repository

Start by forking the project repository to your GitHub account. Make changes in your forked repository and submit a pull request when ready.

### Understand the Project Structure

Before contributing to a project, familiarize yourself with CodeBool's Python project structure.

```
project_root/  
├── core/  
│   ├── generator.py  
│   └── [Other Python Code]   
├── tests/ 
├── cli.py  
├── requirements.txt  
└── README.md  
```

* New feature: Create a new module in `core/` or a new directory, or extend an existing module.
* Bug Fixes: Locate the affected file and modify it directly.
* Tests: Add test cases in the `tests/` directory or expand existing test files.

#### Note:
Do not create folders named after contributors. Track contributions using Git and list contributor information in the `CONTRIBUTORS` file, if necessary.

---

### Build and Test

Before submitting your changes:

* **Build**: Ensure your code compiles without errors.
* **Run Tests**: Verify that all existing tests pass successfully.
* **Add Tests**: Write and run tests for any new functionality.
* **Code Style**: Confirm adherence to the project's coding standards.

Only submit a pull request after all tests pass and your code is fully validated.

---

### Submit a Pull Request

Submit your pull request to the official repository:
[GitHub Repository](https://github.com/LunaStev/codebool)

**Please include the following details if required:**

* **Purpose and functionality** of your changes.
* **Programming language** used.
* **Libraries used** (including any self-developed libraries with detailed explanations).
* **Frameworks used** (including any self-developed frameworks).
* **Technologies or methodologies** applied in your contribution.

Providing detailed information helps maintainers evaluate and integrate your contribution effectively.

---

By adhering to these guidelines, you help maintain the quality, stability, and consistency of the CodeBool project. Thank you for contributing!