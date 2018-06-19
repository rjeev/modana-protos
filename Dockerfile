FROM python:3
MAINTAINER Sharad Baidya

ARG SERVICE_NAME='auth-service'
ARG PORT='5000'
ARG API_URL='http://13.231.170.1:8000/'

ENV SERVICE_NAME=$SERVICE_NAME
ENV PORT=$PORT
ENV API_URL=$API_URL

EXPOSE 5000
COPY src /home/docker/service/
RUN pip install -r /home/docker/service/requirements.txt
WORKDIR /home/docker/service/

CMD ["python", "main.py"]
