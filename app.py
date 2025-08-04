# Flask App
from flask import Flask, render_template, request, jsonify
from openai_config import run_conversation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = run_conversation(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
