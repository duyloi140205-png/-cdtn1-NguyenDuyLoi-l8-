from flask import Flask,jsonify
from dotenv import load_dotenv
from src.routes.survey_routes import bp
load_dotenv()
app=Flask(__name__)
app.json.ensure_ascii = False
app.register_blueprint(bp)
@app.get('/')
def home(): return jsonify(project='L8 CSAT/NPS',status='running',api='/api/surveys')
if __name__ == "__main__":
    app.run(debug=True)
