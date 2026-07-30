# Operational Runbook

## Deploying the application

```bash
kind create cluster --name system-monitor --config kind-config.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml --server-side --force-conflicts
kubectl apply -f argocd-application.yaml
```

## Checking application health

```bash
kubectl get pods
curl http://localhost/api/health
curl http://localhost/api/services
```

## Scaling a component

Edit `monitoring-chart/values.yaml`, change the relevant `replicas` value, then:

```bash
git add monitoring-chart/values.yaml
git commit -m "Scaled <component>"
git push
```

Argo CD automatically applies the change.

## Rolling back a bad deployment

Via Argo CD UI: select the application → **History and Rollback** → choose a previous revision → **Rollback**.

Or via Git: revert the commit and push — Argo CD will sync to the reverted state.

## Restoring the database from backup

```bash
cat backup.sql | kubectl exec -i $(kubectl get pod -l app=database -o jsonpath='{.items[0].metadata.name}') -- psql -U monitor_user -d monitoring_platform
```

## Common issues

**Backend crashes on startup with a database connection error**
Usually a startup race condition — the backend started before PostgreSQL was fully ready. Kubernetes automatically restarts the pod, which typically resolves it on the next attempt.

**`/services` returns an empty list unexpectedly**
The PVC may have been recreated (e.g., after cluster recreation), resulting in a fresh, empty database. Restore from the latest backup if needed.

**Tearing down the environment**
```bash
kind delete cluster --name system-monitor
```