from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
HERE = os.path.abspath(os.path.dirname(__file__))

stations = [
    {"id": 1, "name": "Assembly Line A", "status": "running", "output": 124},
    {"id": 2, "name": "Packaging", "status": "idle", "output": 0}
]

@app.route('/')
def home():
    return send_from_directory(HERE, 'index.html')

@app.route('/api/stations', methods = ["GET"])
def get_stations():
    status = request.args.get('status')
    return jsonify([s for s in stations if not status or s['status'] == status])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
