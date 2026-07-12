#!/bin/bash

set -e

NAMESPACE="home-apps"

echo "========================================="
echo "Deploying Home Server"
echo "========================================="

echo "Creating namespace..."
kubectl create namespace "${NAMESPACE}" \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Updating ConfigMap..."
kubectl create configmap rest-config \
    --from-env-file=/opt/server_deploy/.env.config \
    -n ${NAMESPACE} \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Updating Secret..."
kubectl create secret generic rest-secret \
    --from-env-file=/opt/server_deploy/.env.secret \
    -n ${NAMESPACE} \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Updating Nginx Config..."
kubectl create configmap nginx-config \
    --from-file=k8s/proxy/nginx.conf \
    -n ${NAMESPACE} \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Deploying REST..."
kubectl apply -f k8s/server-rest/ -n ${NAMESPACE} 

echo "Deploying UI..."
kubectl apply -f k8s/server-ui/ -n ${NAMESPACE} 

echo "Deploying Proxy..."
kubectl apply -f k8s/proxy/ -n ${NAMESPACE} 

echo "Waiting for rollout..."

kubectl rollout status deployment/rest -n ${NAMESPACE}
kubectl rollout status deployment/ui -n ${NAMESPACE}
kubectl rollout status deployment/proxy -n ${NAMESPACE}

echo ""
echo "Deployment completed successfully."
echo ""

kubectl get pods -n ${NAMESPACE}
kubectl get svc -n ${NAMESPACE}
