# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-14

### Added
- Initial release of the Final Exam Review Skill.
- Multi-agent collaboration architecture (Agent 1 for generation, Agent 2 for verification).
- Automated course workspace initialization (`materials/`, `result/`).
- Markdown to PDF offline conversion pipeline (`md2pdf.py`).
- Natural-sort Markdown merger script (`md_merger.py`).
- Integrated `Songti.ttc` for 100% offline Chinese PDF rendering.
- A/B Math Mode configuration (Cloud LaTeX rendering vs. Offline Unicode).
- Strict Markdown structural formatting to prevent flattened outlines.
- Question/Answer separation logic for mock exams.

### Security & Robustness
- Bash space-in-path prevention mechanisms (double quotes enforce).
- CJK word-wrap and word-break algorithms enabled in `xhtml2pdf` CSS to prevent text overflow.
- Absolute path enforcement for images to preserve visual integrity during merging.
