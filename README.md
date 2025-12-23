# Code Plagiarism Detector (AST-Based)

## Problem Statement
Traditional text-based plagiarism detectors fail when variable names or formatting are changed.
This project detects plagiarism by comparing the structural logic of programs using Abstract Syntax Trees.

## Key Features
- AST-based structural comparison
- Ignores variable renaming and formatting
- Detects logical similarity
- Web-based interface using Flask

## Tech Stack
- Python
- Flask
- AST (Python built-in module)

## Approach
1. Parse Python code into AST
2. Normalize AST (remove identifiers and literals)
3. Convert AST into node-type sequences
4. Compute similarity using Jaccard similarity

## Similarity Thresholds
- > 85% : Highly Plagiarized
- 60–85% : Partially Similar
- < 60% : Mostly Original

## How to Run
```bash
pip install flask
python app.py
