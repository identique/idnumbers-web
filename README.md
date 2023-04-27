# Checkout our server
https://idnumbers.fly.dev/

# Python
#### Require python version above `3.10`

# Installation
Install dependencies by running
```
pip install -r requirements.txt
```

# Run dev server
(Optional) 1. Replace the `--port 8087` in `./script/dev.sh` to the port you want 
2. Starting the server by running `./scripts/dev.sh`

## Api doc
Api docs can be access in `/docs`
also in our own server https://idnumbers.fly.dev/docs

## Get the Docker image from hub
1. `docker pull identique/identique-web:latest` to get the latest image from docker
2. `docker run -d -p <port_you_want>:8080 --name idnumbers-web identique/identique-web` to run the server