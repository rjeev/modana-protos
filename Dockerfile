FROM python:3
MAINTAINER Sharad Baidya

EXPOSE 5000
COPY src /home/docker/service/
RUN pip install -r /home/docker/service/requirements.txt
WORKDIR /home/docker/service/

CMD ["python", "main.py"]
