from flask import Flask, render_template, request
from ast_utils import parse_code_to_ast, normalize_ast, ast_to_sequence
from similarity import jaccard_similarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None
    message = None

    if request.method == "POST":
        code1 = request.form.get("code1")
        code2 = request.form.get("code2")

        tree1 = parse_code_to_ast(code1)
        tree2 = parse_code_to_ast(code2)

        if tree1 is None or tree2 is None:
            message = "❌ Invalid Python syntax in one of the codes."
        else:
            seq1 = ast_to_sequence(normalize_ast(tree1))
            seq2 = ast_to_sequence(normalize_ast(tree2))

            similarity = jaccard_similarity(seq1, seq2)

            if similarity >= 85:
                message = "⚠️ Highly Plagiarized"
            elif similarity >= 60:
                message = "⚠️ Partially Similar"
            else:
                message = "✅ Mostly Original"

    return render_template("index.html",
                           similarity=similarity,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True)
