# docker_python_rest_api
Dockerizable rest api using python and flask.

## Dependencies
This project needs the following dependencies to run:
* docker
* docker-compose
``` shell script
sudo apt-get install -y docker docker-compose
```

## Installation
The project includes a Makefile so you can the following command:
``` shell script
make install
```
If an error occur try with sudo: 
``` shell script
sudo make install
```

## How to make requests to the API
Using Web Browser (GET):

* http://localhost:5000/finish_stats
* http://localhost:5000/finish_stats/0 where 0 is the id

Note: We recommend "Postman" client to test the rest API (methods POST, Put and DELETE).

Using command line:
```shell script
# GET (obtain the full list of stats).
curl -i http://localhost:5000/finish_stats
# GET (obtain stat by id, where id = 0).
curl -i http://localhost:5000/finish_stats/0
# POST (insert stat).
curl -i -H "Content-Type: application/json" -X POST -d '{"level":1, "player_name": "Delta", "time": 1000}' http://localhost:5000/finish_stats
# PUT (edit stat).
curl -i -H "Content-Type: application/json" -X PUT -d '{"player_name": "Theta"}' http://localhost:5000/finish_stats/0
# DELETE (remove stat).
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/finish_stats/0
```
