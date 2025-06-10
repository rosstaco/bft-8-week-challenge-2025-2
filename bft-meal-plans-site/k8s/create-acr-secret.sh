#!/bin/bash

# Script to create Azure Container Registry secret for MicroK8s
# Usage: ./create-acr-secret.sh <acr-username> <acr-password>

set -e

if [ $# -ne 4 ]; then
    echo "Usage: $0 <acr-username> <acr-password> <>acr-server> <namespace>"
    echo "Example: $0 myusername mypassword myregistry.azurecr.io bft-challenge"
    exit 1
fi

ACR_USERNAME="$1"
ACR_PASSWORD="$2"
ACR_SERVER="$3"
NAMESPACE="$4"

echo "Creating namespace if it doesn't exist..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Creating Azure Container Registry secret..."
kubectl create secret docker-registry azure-registry-secret \
    --docker-server=$ACR_SERVER \
    --docker-username=$ACR_USERNAME \
    --docker-password=$ACR_PASSWORD \
    --namespace=$NAMESPACE \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Secret created successfully!"
echo "You can now deploy using: kubectl apply -k k8s/"
