from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# --- Home page ---
@app.route("/")
def home():
    return render_template("index.html", output_text=None, user_input="")

# --- Input -> Output example ---
@app.route("/echo", methods=["POST"])
def echo():
    text = request.form.get("text", "").strip()
    vibe = request.form.get("vibe", "fun")
    if not text:
        return render_template("index.html", output_text="⚠️ Please enter something!", user_input="")
    tagline = f"{text} — a {vibe} idea for the future 🚀"
    return render_template("index.html", output_text=tagline, user_input=text)

# --- API: Advice ---
@app.route("/api/advice")
def advice():
    try:
        r = requests.get("https://api.adviceslip.com/advice", timeout=10)
        data = r.json()
        return jsonify({"advice": data["slip"]["advice"]})
    except Exception:
        return jsonify({"advice": "Could not fetch advice this time."}), 500

# --- API: Dog image ---
@app.route("/api/dog")
def dog():
    try:
        r = requests.get("https://dog.ceo/api/breeds/image/random", timeout=10)
        data = r.json()
        return jsonify({"image": data["message"]})
    except Exception:
        return jsonify({"image": None}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
