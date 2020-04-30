Now that we have an application ready to be containerized, we need to write a Dockerfile to build an image.

## Task



```dockerfile
FROM ubuntu:latest
COPY ./request.py /deploy/
COPY ./model.pkl /deploy/
WORKDIR /deploy/
RUN pip install flask sklearn pandas seaborn matplotlib
EXPOSE 80
ENTRYPOINT ["python3", "request.py"]
```



Build the docker image required by running the command:

`docker build --tag iris_app . `{{execute}}

