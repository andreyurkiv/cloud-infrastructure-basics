# Cloud infrastructure basics homework

## Part 1: Running basic service 

To be able to work with the basic service you need to do the following steps:

1) Navigate to the project directory (where `Dockerfile` is located)

2) Create Docker image 

`docker build --tag=factor:latest .`

2) Run Docker image 

`docker run -p 4000:80 factor`

3) Open your browser and type in address `0.0.0.0:4000/`

4) Perform integer number factorization using the service

* In order to load the service for ~ 10 minutes you need to type in number `100000000000000000001`


## Running service on Kubernetes using local Docker repository

First, you need to make sure that your Kubernetes cluster is up and running

1) If needed, remove your current minikube cluster

`minikube delete`

2) And start new minikube cluster 

`minikube start`

3) Run bash script to automatically deploy the app to Kubernetes

`./installation-local.sh`

4) Open service in browser using the `webapp` adrress from

`minikube service list`


## Running service on Kubernetes using cloud repository

First, make sure that your Kubernetes cluster is up and running.

If needed, repeat steps 1 and 2 from previous section.

1) Run the script to automatically deploy th app to Kubernetes

`./installation-cloud.sh`

2) Open service in browser using the `webapp` adrress from

`minikube service list`

## Liveness/Readyness check - present in both versions (please take a look in `.yaml` files)
