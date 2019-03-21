#!/bin/bash

# Deploy app to Kubernetes

kubectl create -f deployment-cloud.yaml

kubectl create -f webapp-expose.yaml
