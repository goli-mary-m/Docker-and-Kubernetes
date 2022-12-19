# Docker and Kubernetes

The second project of Cloud Computing using Docker and Kubernetes.

## Section-1:

- Building a docker image based on ubuntu for running curl commands

- Publishing this docker image to Docker Hub [(maryamgoli/curl-ubuntu)](https://hub.docker.com/repository/docker/maryamgoli/curl-ubuntu)

- Testing docker image with pulling it from Docker Hub 


## Section-2:
- Implementing a flask server that uses redis for storing names and prices of cryptocurrencies

   
    -> configurable values that are defined as environment variables:
     
    1. PORT: server port - [default: 5000]
    2. API_KEY: API key from [Coinapi.io](https://www.coinapi.io/)
    3. CRYPTOCURRENCY_NAME: name of the cryptocurrency that we want its price - [default: "btc"]
    4. EXPIRATION_TIME_MINUTE: the expiration time (in minutes) for redis data - [default: 5]
     

- Building docker image of flask server and publishing this docker image to Docker Hub [(maryamgoli/flaskserver)](https://hub.docker.com/repository/docker/maryamgoli/flaskserver) 

- Running flaskserver image as a container
(we can change the value of environment variables with switch "--env")

  ```bash
  > docker run -d -it -p 5000:5000 --network my-network --name flaskserver maryamgoli/flaskserver:1.0
  > docker run -d -it --env EXPIRATION_TIME_MINUTE=3 -p 5000:5000 --network my-network --name flaskserver maryamgoli/flaskserver:1.0
   ```

- Pulling redis image from registry and running redis image as a container
  ```bash
  > docker pull redis
  > docker run -d -p 6379:6379 --name my-redis --volume my-volume:/data --network my-network redis
  ```

- Sending request to flaskserver
  ```bash
  > curl -X GET localhost:5000
  ```
