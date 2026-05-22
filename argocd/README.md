# ArgoCD GitOps setup (local Helm demo)

This folder contains ArgoCD Application manifests to deploy the ecommerce Helm chart.

## Notes
- This environment uses `repoURL: file:///home/cis/ai-devops-project` so ArgoCD can read the chart directly from the local filesystem.
- For a real GitOps workflow, change `repoURL` to your Git repository URL and `path` accordingly.

## Apply
```bash
kubectl apply -f argocd/
```

