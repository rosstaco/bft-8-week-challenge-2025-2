# BFT Meal Plans - Kubernetes Deployment

This directory contains Kubernetes manifests and Kustomize configuration for deploying the BFT Meal Plans Docusaurus site to a MicroK8s cluster.

## Prerequisites

1. **MicroK8s cluster** running with the following addons enabled:
   ```bash
   microk8s enable dns
   microk8s enable ingress
   microk8s enable cert-manager  # Optional, for TLS certificates
   ```

2. **kubectl** configured to connect to your MicroK8s cluster:
   ```bash
   microk8s kubectl config view --raw > ~/.kube/config
   # or use microk8s kubectl directly
   ```

3. **kustomize** installed (optional, kubectl has built-in kustomize support)

4. **Azure Container Registry credentials** for pulling the container image

## Quick Deployment

### Option 1: Using the deployment script (Recommended)
```bash
cd k8s
./deploy.sh <your-acr-username> <your-acr-password>
```

### Option 2: Manual deployment
```bash
# 1. Create the registry secret
./create-acr-secret.sh <your-acr-username> <your-acr-password>

# 2. Deploy using kubectl with kustomize
kubectl apply -k .

# 3. Check deployment status
kubectl get all -n bft-challenge
```

## Configuration

### Container Image
- **Registry**: `rossmiles-a7gvddc7fcfkc0d3.azurecr.io`
- **Image**: `experements/bft-meal-plans:latest`
- **Pull Secret**: `azure-registry-secret`

### Networking
- **Namespace**: `bft-challenge`
- **Service**: `bft-meal-plans-service` (ClusterIP on port 80)
- **Ingress**: `bft-challenge.fish-taco.net`
- **TLS**: Enabled with cert-manager (letsencrypt-prod issuer)

### Resources
- **Replicas**: 2 (for high availability)
- **CPU**: 50m request, 100m limit
- **Memory**: 64Mi request, 128Mi limit
- **Health Checks**: Liveness and readiness probes on `/`

## Files Structure

```
k8s/
├── kustomization.yaml     # Main Kustomize configuration
├── namespace.yaml         # Namespace definition
├── deployment.yaml        # Deployment manifest
├── service.yaml          # Service manifest  
├── ingress.yaml          # Ingress manifest
├── create-acr-secret.sh  # Script to create registry secret
├── deploy.sh             # Main deployment script
└── README.md             # This file
```

## Useful Commands

### Check deployment status
```bash
kubectl get all -n bft-challenge
```

### View logs
```bash
kubectl logs -f deployment/bft-meal-plans -n bft-challenge
```

### Scale deployment
```bash
kubectl scale deployment bft-meal-plans --replicas=3 -n bft-challenge
```

### Update image
```bash
# Edit kustomization.yaml to change the image tag, then:
kubectl apply -k .
```

### Delete deployment
```bash
kubectl delete -k .
# or
kubectl delete namespace bft-challenge
```

## Troubleshooting

### Image pull errors
1. Verify ACR credentials are correct
2. Check if the secret exists: `kubectl get secret azure-registry-secret -n bft-challenge`
3. Recreate the secret: `./create-acr-secret.sh <username> <password>`

### Ingress not working
1. Ensure MicroK8s ingress addon is enabled: `microk8s status`
2. Check ingress controller: `kubectl get pods -n ingress`
3. Verify DNS resolution for `bft-challenge.fish-taco.net`

### Pod not starting
1. Check pod status: `kubectl describe pod -l app=bft-meal-plans -n bft-challenge`
2. Check events: `kubectl get events -n bft-challenge --sort-by='.lastTimestamp'`

## Security Notes

- Containers run as non-root user (UID 1001)
- Security context drops all capabilities
- ReadOnlyRootFilesystem is disabled for nginx to write temp files
- Resource limits prevent resource exhaustion

## Customization

To customize the deployment:

1. **Change image tag**: Edit `newTag` in `kustomization.yaml`
2. **Modify resources**: Edit `deployment.yaml` resources section
3. **Update domain**: Change host in `ingress.yaml`
4. **Add environment variables**: Edit `deployment.yaml` env section

## TLS Certificate

The ingress is configured to use cert-manager with Let's Encrypt. If you don't have cert-manager installed:

1. Install cert-manager:
   ```bash
   microk8s enable cert-manager
   ```

2. Or remove TLS configuration from `ingress.yaml` for HTTP-only access
