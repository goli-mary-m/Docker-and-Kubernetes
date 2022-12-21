from flask import Flask, request
from redis import Redis
import os
import requests
import socket

# environment variables
port = os.environ.get('PORT', 5000)
api_key = os.environ.get('API_KEY', "YOUR_API_KEY")
cryptocurrency_name = os.environ.get('CRYPTOCURRENCY_NAME', "btc")
expiration_time_minute = os.environ.get('EXPIRATION_TIME_MINUTE', 5)


app = Flask(__name__)
myredis = Redis(host="redis-service", port=6379)

@app.route("/", methods=["GET"])
def main_page():

    if request.method == "GET":

        id = str(cryptocurrency_name)

        if(myredis.exists(id)):
            # get data from redis
            name = str(myredis.get(id).decode("utf-8"))
            price = str(myredis.get(name).decode("utf-8"))
        else:
            # send request to coinapi.io
            coinapi_url = "https://rest.coinapi.io/v1/assets/" + str(id)
            coinapi_headers = {'X-CoinAPI-Key' : api_key}
            coinapi_response = (requests.get(coinapi_url, headers=coinapi_headers)).json()[0]
        
            name = str(coinapi_response.get('name'))
            price = str(coinapi_response.get('price_usd'))

            # add data to redis
            expiration_time_sec = int(float(expiration_time_minute)*60.0)
            myredis.set(id, name, ex=expiration_time_sec)
            myredis.set(name, price, ex=expiration_time_sec)

        hostname = socket.gethostname()
        response = {'name' : name, 'price' : price, 'hostname' : hostname}
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(port), debug=True)