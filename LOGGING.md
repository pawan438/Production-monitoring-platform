# Logging Setup

This project uses Loki and Promtail for centralized log collection, alongside the existing Grafana instance from the monitoring stack.

## Installation

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install loki grafana/loki-stack -n monitoring \
  --set grafana.enabled=false \
  --set prometheus.enabled=false
```

This installs:
- **Loki** — log aggregation backend
- **Promtail** — DaemonSet that collects logs from every node and ships them to Loki

## Verifying Loki is running

```bash
kubectl get pods -n monitoring -l release=loki
kubectl get svc -n monitoring | grep loki
```

## Connecting Loki to Grafana

1. Open Grafana → **Connections** → **Data sources** → **Add data source**
2. Select **Loki**
3. URL: `http://loki:3100`
4. Save & test

## Viewing logs

1. Grafana → **Explore**
2. Select **Loki** as the data source
3. Filter by label, e.g. `namespace="default"` or `app="backend"`
4. Run query to view live logs