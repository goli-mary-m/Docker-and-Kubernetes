# Docker and Kubernetes

The second project of Cloud Computing using Docker and Kubernetes.

## Section-1: 

- Building a docker image based on ubuntu for running curl commands

- Publishing this docker image to Docker Hub [(maryamgoli/curl-ubuntu)](https://hub.docker.com/repository/docker/maryamgoli/curl-ubuntu)

- Testing docker image by pulling it from Docker Hub 

## Section-2:
- Implementing a flask server that uses redis for storing names and prices of cryptocurrencies

   
    configurable values that are defined as environment variables:
     
    - PORT: server port - [default: 5000]
    - API_KEY: API key from [Coinapi.io](https://www.coinapi.io/)
    - CRYPTOCURRENCY_NAME: name of the cryptocurrency that we want its price - [default: "btc"]
    - EXPIRATION_TIME_MINUTE: the expiration time (in minutes) for redis data - [default: 5]


- Building docker image of flask server and publishing this docker image to Docker Hub [(maryamgoli/flaskserver)](https://hub.docker.com/repository/docker/maryamgoli/flaskserver) 

- Running flaskserver image as a container

  ```bash
  $ docker run -d -it -p 5000:5000 --network my-network --name flaskserver maryamgoli/flaskserver:1.0
  ```
    we can change the value of environment variables with "--env" option:

   ```bash
  $ docker run -d -it --env EXPIRATION_TIME_MINUTE=3 -p 5000:5000 --network my-network --name flaskserver maryamgoli/flaskserver:1.0
   ```

- Pulling redis image from registry and running redis image as a container
  ```bash
  $ docker pull redis
  $ docker run -d -p 6379:6379 --name my-redis --volume my-volume:/data --network my-network redis
  ```

- Sending request to flaskserver
  ```bash
  $ curl localhost:5000
  ```

## Section-3:

- Building docker image of updated flaskserver (for using in Kubernetes) and publishing this docker image to Docker Hub [(maryamgoli/flaskserver-k8s)](https://hub.docker.com/repository/docker/maryamgoli/flaskserver-k8s) 

- Using minikube for deploying our application on Kubernetes cluster 

  ```bash
  $ minikube start
  $ alias kubectl="minikube kubectl --"
  ```
     __flaskserver:__ 

     ```bash
     $ kubectl apply -f flaskserver-configmap.yaml
     $ kubectl apply -f flaskserver-deployment.yaml
     $ kubectl apply -f flaskserver-service.yaml
     ```

    __redis:__ 

     ```bash
     $ kubectl apply -f redis-persistentvolume.yaml
     $ kubectl apply -f redis-persistentvolumeclaim.yaml
     $ kubectl apply -f redis-deployment.yaml
     $ kubectl apply -f redis-service.yaml
     ```

## Section-4:

- Creating a pod using [curl-ubuntu](https://hub.docker.com/repository/docker/maryamgoli/curl-ubuntu) image and testing the server

     ```bash
     $ kubectl run curl-pod --image=maryamgoli/curl-ubuntu:1.0 -it
     root@curl-pod:/# curl flaskserver-service
    {
      "hostname": "flaskserver-78f5757657-jssrc",
      "name": "Bitcoin",
      "price": "16828.237904807465"
    }
     ```
