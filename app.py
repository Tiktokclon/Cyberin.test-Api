from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint de test pour voir si l'API répond
@app.route("/v1/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "message": "API opérationnelle"}), 200

# Endpoint pour simuler un modèle (compatible OpenAI)
@app.route("/v1/completions", methods=["POST"])
def completions():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "")

    # Simulation de réponse (tu pourras brancher ton vrai modèle ici)
    return jsonify({
        "id": "cmpl-test-001",
        "object": "text_completion",
        "choices": [
            {"text": f"Réponse générée pour: {prompt}"}
        ]
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
