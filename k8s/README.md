# Kubernetes manifests - Ecommerce (FastAPI + Vanilla JS)

## Files
- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`

## Notes
- The Deployment uses image `ai-devops-project-web:latest` (local). For real clusters, push to a registry and update the image.
- JWT secret is set via env var `JWT_SECRET=change-me`.
- Ingress host is `ecommerce.local` (change as needed).

## Apply
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

## Test
- `kubectl get pods -l app=ecommerce`
- `kubectl get svc ecommerce`


