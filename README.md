# AI-Driven GitOps Ecommerce Deployment Platform

Production-grade GitOps CI/CD ecommerce deployment platform built using Kubernetes, Docker, Helm, ArgoCD, and GitHub Actions.

## 🚀 Features

- Automated CI/CD pipeline using GitHub Actions
- GitOps deployment workflow with ArgoCD
- Automatic Docker image versioning (v1 → v2 → v3...)
- Kubernetes rolling deployments
- Helm-based application deployment
- FastAPI backend with JWT authentication
- Frontend + Backend containerized deployment
- Horizontal Pod Autoscaler (HPA)
- Persistent Volumes (PV/PVC)
- Kubernetes Ingress
- Network Policies
- Automated DockerHub image publishing

---

## 🛠 Tech Stack

- Kubernetes
- Docker
- Helm
- ArgoCD
- GitHub Actions
- FastAPI
- Python
- Linux
- DockerHub
- YAML
- GitOps

---

## ⚙️ CI/CD Workflow

```text
Developer Pushes Code
        ↓
GitHub Actions Trigger
        ↓
Docker Image Build
        ↓
Auto Version Tagging (v1/v2/v3)
        ↓
Push Image to DockerHub
        ↓
Update Helm values.yaml
        ↓
Commit Changes Back to GitHub
        ↓
ArgoCD Detects Changes
        ↓
Kubernetes Auto Sync
        ↓
Rolling Deployment
