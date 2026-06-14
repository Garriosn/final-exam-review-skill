# Final Exam Review Agent Skill

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Offline Capable](https://img.shields.io/badge/offline-100%25-brightgreen)
![Agents](https://img.shields.io/badge/agents-multi--agent-orange)

An AI Agent Skill designed to act as an extremely powerful teacher. It helps students learn course content, summarizes key points into readable outlines, and automatically generates mock exams. It utilizes multi-agent collaboration to ensure accuracy and high-quality outputs.

---

## 📸 Screenshots

*(Replace these placeholders with actual screenshots of your Agent generating outlines and PDFs)*
- `![Outline Generation](./examples/outline_screenshot.png)`
- `![Mock Exam Output](./examples/exam_screenshot.png)`

---

## ✨ Features
- 📂 **Automated Workspace Management**: Sets up an organized directory structure for your course materials.
- 📝 **Smart Outlines**: Extracts knowledge points from your courseware and generates readable Markdown (`.md`) summaries.
- 🎓 **Mock Exams**: Randomly selects key points to generate customized mock exams with answers and explanations.
- 🤖 **Multi-Agent Verification**: Uses a dual-agent system (Generator & Checker) to ensure the accuracy and rigor of all study materials.
- 🖨️ **Zero-Config PDF Engine**: Automatically compiles the final outlines and exams into beautifully formatted PDFs, complete with Chinese font support.
- 📐 **Math Mode A/B**: Choose between high-fidelity cloud LaTeX rendering or bulletproof offline text-based math formulas.

---

## 🛠 Requirements

- **Agent Framework**: An AI Agent system capable of executing `.md` skills and running `python3` commands in a terminal.
- **Python Environment**: Python 3.8+ installed on the host machine.
- **Network**: Internet access is **ONLY** required for the initial run to automatically install Python dependencies (`markdown`, `xhtml2pdf`), or if you select **Math Mode A** (Cloud rendering). Everything else is 100% offline.

---

## 🚀 Installation

### Absolute Zero Configuration
This skill requires **ZERO** manual configuration or terminal commands to run. 

- No need to run `brew install`.
- No need to run `pip install`.
- No need to worry about `pip` vs `pip3` conflicts.

When the Agent processes your materials for the first time, its internal scripts will use `sys.executable` to **autonomously detect, download, and securely install** all necessary pure-Python dependencies straight into the correct environment. It's completely hands-free!

### How to Install the Skill itself
Simply copy this entire `final-exam-review-skill` directory into your Agent's plugins folder (e.g., `~/.gemini/config/plugins/`).

---

## 💡 Usage

Simply ask your Agent:
> "我需要复习期末考试，帮我建立一下文件夹结构，课程名称是《高级人工智能》。"

Once the folders are created and you've placed your courseware in the `materials/Courseware` folder, tell the Agent:
> "资料上传完了，开始整理。"

See the [`examples/interaction_example.md`](examples/interaction_example.md) file for a complete walkthrough of a conversation with the Agent.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
