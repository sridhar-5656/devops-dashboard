# pyrefly: ignore [missing-import]
from flask import Flask, render_template

app = Flask(__name__, template_folder="template")


@app.route("/")
def home():
    return render_template(
        "index.html",
        version="v1.0.0",
        environment="Development",
        deployment="Docker"
    )


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "DevOps Deployment Dashboard"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
