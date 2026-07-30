# Production System Monitoring Platform

A production-style monitoring platform built as the capstone project for the "60 Days of Learning" DevOps program at Leapfrog Technology. It simulates a real Site Reliability Engineering (SRE) platform — monitoring servers, containers, and Kubernetes workloads from a centralized dashboard.

## Overview

This platform demonstrates a full production DevOps workflow: containerized services, Kubernetes deployment, GitOps-based delivery, observability, and disaster recovery — all built incrementally over the course of the capstone.

See [ARCHITECTURE.md](./ARCHITECTURE.md) for a full system diagram and component breakdown.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes (kind)
- **Package Management:** Helm
- **GitOps:** Argo CD
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus, Grafana
- **Logging:** Loki, Promtail

## Repository Structure
production-monitoring-platform/
├── backend/ # Flask API
├── frontend/ # Static frontend
├── k8s/ # Raw Kubernetes manifests
├── monitoring-chart/ # Helm chart for the full stack
├── .github/workflows/ # CI pipeline
├── argocd-application.yaml
├── kind-config.yaml
├── docker-compose.yml
├── ARCHITECTURE.md
├── RUNBOOK.md
├── MONITORING.md
├── LOGGING.md
└── DISASTER-RECOVERY.md

## Getting Started

See [RUNBOOK.md](./RUNBOOK.md) for full deployment and operational instructions.

Quick start:

```bash
kind create cluster --name system-monitor --config kind-config.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml --server-side --force-conflicts
kubectl apply -f argocd-application.yaml
```

Once deployed:
```bash
curl http://localhost/api/health
```

## Documentation

- [Architecture](./ARCHITECTURE.md)
- [Runbook](./RUNBOOK.md)
- [Monitoring Setup](./MONITORING.md)
- [Logging Setup](./LOGGING.md)
- [Disaster Recovery](./DISASTER-RECOVERY.md)

## Project Journey

This platform was built incrementally across Days 45–60 of the 60 Days of Learning program, covering:

- Backend API development and database integration
- Frontend development
- Containerization with Docker
- CI/CD with GitHub Actions
- Kubernetes deployment, security hardening, and networking
- Helm packaging
- GitOps delivery with Argo CD
- Monitoring and logging
- Disaster recovery