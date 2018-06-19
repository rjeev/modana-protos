#!/usr/bin/env bash
docker image prune -f
docker build -t auth-service --build-arg SERVICE_NAME=$SERVICE_NAME \
                     --build-arg PORT=$PORT  \
                     --build-arg API_URL=$API_URL \
                     -f ../../Dockerfile ../../

echo "**************Build Successfull**************"

docker run -d -p 5000:5000 --name=auth-service auth-service

echo "**************Run Successfull****************"