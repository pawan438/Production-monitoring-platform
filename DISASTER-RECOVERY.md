# Disaster Recovery

This document covers backup and recovery procedures for the Production System Monitoring Platform.

## Database Backup

```bash
kubectl exec -it $(kubectl get pod -l app=database -o jsonpath='{.items[0].metadata.name}') -- pg_dump -U monitor_user -d monitoring_platform > backup.sql
```

This creates a full SQL dump of the database, including schema and data, stored outside the cluster.

## Database Restore

```bash
cat backup.sql | kubectl exec -i $(kubectl get pod -l app=database -o jsonpath='{.items[0].metadata.name}') -- psql -U monitor_user -d monitoring_platform
```

## Infrastructure Recovery

Since all Kubernetes manifests are managed via Argo CD (GitOps), infrastructure automatically self-heals if resources are deleted — Argo CD detects drift from Git and recreates missing Deployments, Services, ConfigMaps, Secrets, and PVCs without manual intervention.

**Note:** infrastructure self-healing recreates resource *definitions*, not data. PVC data must be restored separately from a backup.

## Tested Recovery Scenario

1. Backed up the database using `pg_dump`
2. Deleted the database Deployment and PVC (simulating total data loss)
3. Argo CD automatically recreated the Deployment and a new empty PVC
4. Restored data from the backup file
5. Verified the API returned all original data correctly