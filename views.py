from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)


# Перевірка працездатності застосунку
@app.route('/healthz/live', methods=['GET'])
def liveness_check():
    return jsonify({
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


# Перевірка готовності застосунку
@app.route('/healthz/ready', methods=['GET'])
def readiness_check():
    return jsonify({
        "status": "ready",
        "database": "not_connected_yet",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)