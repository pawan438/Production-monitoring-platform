# app.py
# Backend API for the Production System Monitoring Platform
# Day 47: connected to PostgreSQL, /services now reads from the database
# Day 48: added CORS support so the frontend can call this API
# Day 53: prefixed all routes with /api for Ingress routing

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# Database connection settings
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "monitoring_platform")
DB_USER = os.environ.get("DB_USER", "monitor_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "monitor_pass")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            uptime_seconds INTEGER NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# Root route - just confirms the API is alive and gives basic info
@app.route("/api/")
def index():
    return jsonify({
        "service": "production-monitoring-platform-backend",
        "status": "running"
    })

# Health check route - used by Kubernetes liveness/readiness probes
@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"}), 200

# Services route - reads from the PostgreSQL database
@app.route("/api/services")
def services():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, status, uptime_seconds FROM services;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = [
        {"name": row[0], "status": row[1], "uptime_seconds": row[2]}
        for row in rows
    ]
    return jsonify(result), 200

# Metrics route - placeholder for now
@app.route("/api/metrics")
def metrics():
    return jsonify({"message": "metrics endpoint placeholder, coming soon"}), 200

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)