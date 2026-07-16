# app.py
# Backend API for the Production System Monitoring Platform
# Day 46: added /services and /metrics routes with mock data

from flask import Flask, jsonify

app = Flask(__name__)

# Root route - just confirms the API is alive and gives basic info
@app.route("/")
def index():
    return jsonify({
        "service": "production-monitoring-platform-backend",
        "status": "running"
    })

# Health check route - used by Kubernetes liveness/readiness probes later
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

# Services route - returns a list of monitored services
# For now this is mock/hardcoded data. Later this will come from a database.
@app.route("/services")
def services():
    monitored_services = [
        {"name": "backend-api", "status": "up", "uptime_seconds": 3600},
        {"name": "frontend", "status": "up", "uptime_seconds": 3550},
        {"name": "database", "status": "up", "uptime_seconds": 7200},
        {"name": "cache-service", "status": "down", "uptime_seconds": 0}
    ]
    return jsonify(monitored_services), 200

# Metrics route - placeholder for now
# Later this will expose real metrics for Prometheus to scrape
@app.route("/metrics")
def metrics():
    return jsonify({"message": "metrics endpoint placeholder, coming soon"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)