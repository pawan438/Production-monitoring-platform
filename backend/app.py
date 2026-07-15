# app.py
# Backend API for the Production System Monitoring Platform

from flask import Flask, jsonify

app = Flask(__name__)

# Root route - just confirms the API is alive and gives basic info
@app.route("/")
def index():
    return jsonify({
        "service": "production-monitoring-platform-backend",
        "status": "running"
    })

# Health check route - this will later be used by Kubernetes
# liveness/readiness probes, so keep it lightweight and fast
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # 0.0.0.0 so it's reachable from outside the container later on
    app.run(host="0.0.0.0", port=5000)