from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", output_text=None, user_input="")

@app.route("/echo", methods=["POST"])
def echo():
    text = request.form.get("text", "").strip()
    if not text:
        return render_template("index.html", output_text="Please enter something!", user_input="")
    tagline = f"{text} — a fun workshop idea!"
    return render_template("index.html", output_text=tagline, user_input=text)

@app.route("/api/advice")
def advice():
    r = requests.get("https://api.adviceslip.com/advice", timeout=10)
    data = r.json()
    return jsonify({"advice": data.get("slip", {}).get("advice", "No advice")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
