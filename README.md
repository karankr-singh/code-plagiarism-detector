🔍 AST-Based Code Plagiarism Detector

A Python-based plagiarism detection system that identifies **logical similarity** between source codes using **Abstract Syntax Trees (AST)** instead of plain text comparison.

📸 Screenshot

<img width="1341" height="626" alt="Screenshot 2025-12-23 215403" src="https://github.com/user-attachments/assets/8fab12ff-1376-4d39-80ec-03ceedfbc1aa" />


📌 Problem Statement

Traditional plagiarism detection tools rely on text comparison, which fails when:
- Variable names are renamed
- Code formatting is changed
- Comments are removed or added

This project solves the problem by analyzing the **structural logic** of programs using **AST**, making it robust against superficial changes.

---

🚀 Key Features

- AST-based structural code comparison
- Ignores variable names, function names, and literals
- Detects logical plagiarism even after renaming identifiers
- Web-based interface using Flask
- Clear plagiarism percentage with verdict

---

🛠️ Tech Stack

- **Python**
- **Flask** – Web framework
- **AST (Abstract Syntax Tree)** – Built-in Python module
- **Git & GitHub** – Version control

---

🧠 System Architecture

```

User Input (Python Code)
↓
AST Parsing (ast.parse)
↓
AST Normalization
(Remove identifiers & literals)
↓
AST → Node Type Sequence
↓
Jaccard Similarity Calculation
↓
Plagiarism Percentage + Verdict

````

---

⚙️ How It Works

1. The source code is parsed into an Abstract Syntax Tree.
2. The AST is normalized by replacing:
   - Variable names → VAR
   - Function names → FUNC
   - Literal values → CONST
3. The normalized AST is converted into a sequence of node types.
4. Jaccard similarity is computed between two sequences.
5. A plagiarism percentage and verdict are generated.

---

📊 Similarity Thresholds

| Similarity % | Verdict |
|-------------|--------|
| > 85% | Highly Plagiarized |
| 60–85% | Partially Similar |
| < 60% | Mostly Original |

---

▶️ How to Run the Project

1️⃣ Install Dependencies
```bash
pip install flask
````

2️⃣ Run the Application

```bash
python app.py
```

3️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

Paste two Python codes and check similarity.

---

🧪 Example Use Case

Code snippets with renamed variables but identical logic will still show high similarity:

```python
def add(a, b):
    return a + b
```

```python
def sum(x, y):
    return x + y
```

---

❗ Limitations

* Currently supports **Python only**
* Does not detect semantic equivalence using different algorithms
* Cannot compare across different programming languages

---

🔮 Future Enhancements

* Support for multiple programming languages
* Tree Edit Distance for deeper structural comparison
* File upload support (.py files)
* Highlight plagiarized code sections
* Multi-file project comparison

---

👨‍💻 Author

**Karan Kumar Singh**
