# Contributing

First off, thank you for considering contributing to the Final Exam Review Agent Skill! It's people like you that make the open-source community such a great place to learn, inspire, and create.

## How to Contribute

1. **Fork the Repository**: Start by forking the project to your own GitHub account.
2. **Clone the Repo**: Clone your forked repository to your local machine.
3. **Create a Branch**: Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
4. **Make Changes**: Implement your changes. Make sure to test them locally within your AI Agent environment.
5. **Commit**: Commit your changes with a descriptive commit message (`git commit -m 'Add some feature'`).
6. **Push**: Push your branch to your fork (`git push origin feature/your-feature-name`).
7. **Submit a Pull Request**: Open a Pull Request from your fork to the main repository.

## Development Guidelines

- **Prompt Engineering**: If you are modifying `SKILL.md`, please ensure the instructions remain clear, concise, and leave no room for ambiguity. Test edge cases (e.g., spaces in paths, weird markdown formatting).
- **Python Scripts**: Ensure that `scripts/md_merger.py` and `scripts/md2pdf.py` remain as standard and robust as possible. 
  - Do not introduce external binary dependencies unless absolutely necessary.
  - Rely on `sys.executable` for `pip` installs to maintain the "Zero-Config" philosophy.
- **Reporting Bugs**: If you find a bug, please open an issue and include:
  - Your operating system.
  - The AI Agent framework you are using.
  - Steps to reproduce the bug.
  - Expected vs actual behavior.

Thank you for contributing!
