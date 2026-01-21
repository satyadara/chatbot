# backend/app.py

from flask import Flask, request, jsonify
from memory import VectorMemory
from reasoning import explain_reasoning

app = Flask(__name__)
memory = VectorMemory()

# Sample data (acts like company documents)
memory.store(
    "Company data retention policy requires storing data for 5 years.",
    {"department": "Compliance", "year": 2024}
)

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("message")

    context = memory.retrieve(user_query)
    answer = "This is a placeholder response until the LLM is connected."

    reasoning = explain_reasoning(context)

    return jsonify({
        "answer": answer,
        "reasoning": reasoning
    })

if __name__ == "__main__":
    app.run(debug=True)
