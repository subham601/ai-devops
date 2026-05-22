# Helm chart: ecommerce

Install:
  helm upgrade --install ecommerce ./helm/ecommerce -n ecommerce-system --create-namespace

Then verify:
  kubectl -n ecommerce-system get deploy,svc,ingress,pods,hpa,pvc

