# Monitoring Setup

This project uses `kube-prometheus-stack` for cluster and application monitoring (Prometheus, Grafana, Alertmanager).

## Installation

```bash
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring-stack prometheus-community/kube-prometheus-stack -n monitoring
```

## Accessing Grafana

```bash
kubectl --namespace monitoring get secrets monitoring-stack-grafana -o jsonpath="{.data.admin-password}" | base64 -d
kubectl --namespace monitoring port-forward svc/monitoring-stack-grafana 3000:80
```

Visit `http://localhost:3000`, login as `admin` with the password above.

## Accessing Prometheus

```bash
kubectl port-forward svc/monitoring-stack-kube-prom-prometheus 9090:9090 -n monitoring
```

Visit `http://localhost:9090`.