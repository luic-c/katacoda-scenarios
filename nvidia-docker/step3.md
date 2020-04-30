Now that we have an application ready to be containerized, we need to write a Dockerfile to build an image.

## Task



```dockerfile
FROM python:3.6
COPY ./request.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "request.py"]
```



Build the docker image required by running the command:

`docker build --tag iris_app . `{{execute}}

