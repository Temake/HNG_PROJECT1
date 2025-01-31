from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS  
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app) 
api=Api(app)

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "teminioluwaopemipo@gmail.com",  
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/Temake/HNG_PROJECT1",
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
