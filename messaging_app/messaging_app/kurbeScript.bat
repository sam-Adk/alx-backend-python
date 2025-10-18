@echo off
echo 🚀 Starting Kubernetes cluster using Minikube...
minikube start

echo ✅ Checking cluster info...
kubectl cluster-info

echo 📦 Retrieving available pods...
kubectl get pods -A

echo 🎉 Kubernetes cluster setup complete!
pause
