import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from dotenv import load_dotenv
from src.routes.survey_routes import bp
from src.routes.auth_routes import auth_bp

load_dotenv()
load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

if not app.config["SECRET_KEY"]:
    raise RuntimeError("Thiếu SECRET_KEY trong file .env")
app.json.ensure_ascii = False
app.register_blueprint(bp)
app.register_blueprint(auth_bp)

@app.get("/")
def home():
    return jsonify(
        project="L8 CSAT/NPS",
        status="running",
        api="/api/surveys"
    )


if __name__ == "__main__":
   if __name__ == "__main__":
    app.run(debug=False)