#!/bin/bash

# Deploy app to Kubernetes

eval $(minikube docker-env)

docker build -t cib/factor:latest .

kubectl create -f deployment-local.yaml

kubectl create -f webapp-expose.yaml