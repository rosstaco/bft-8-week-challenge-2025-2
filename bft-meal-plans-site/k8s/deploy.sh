#!/bin/bash

# Deployment script for BFT Meal Plans to MicroK8s
# Usage: ./deploy.sh [acr-username] [acr-password]

set -e

echo "🚀 Deploying BFT Meal Plans to MicroK8s..."

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    exit 1
fi


# Create ACR secret if credentials provided
if [ $# -eq 2 ]; then
    echo "📝 Creating Azure Container Registry secret..."
    ./create-acr-secret.sh "$1" "$2"
else
    echo "⚠️  No ACR credentials provided. Make sure azure-registry-secret exists in bft-challenge namespace."
    echo "   If not, run: ./create-acr-secret.sh <username> <password>"
fi

# Apply the kustomization
echo "📦 Applying Kubernetes manifests..."
kubectl apply -k .

# Wait for deployment to be ready
echo "⏳ Waiting for deployment to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/bft-meal-plans -n bft-challenge

# Get deployment status
echo "✅ Deployment status:"
kubectl get pods -n bft-challenge -l app=bft-meal-plans

echo ""
echo "🌐 Service information:"
kubectl get service bft-meal-plans-service -n bft-challenge

echo ""
echo "🔗 Ingress information:"
kubectl get ingress bft-meal-plans-ingress -n bft-challenge

echo ""
echo "🎉 Deployment complete!"
echo ""
echo "📊 To check logs: kubectl logs -f deployment/bft-meal-plans -n bft-challenge"
echo "🔍 To check status: kubectl get all -n bft-challenge"
