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



Build the docker image `iris_app` required by running the command:

`docker build --tag iris_app . `{{execute}}

To run the image as container, run the following command to start the terminal in the container:

`docker run -it iris_app /bin/bash  `{{execute}}

To check whether the container is running, run the command:

`docker container ls  `{{execute}}

The terminal will show that the container is running and up for (...) minutes.



_Fun Fact: Notice that there is also a NAMES column besides Container ID. It can be used interchangeably as the ID as it is more readable to human. The name generator is actually written in Go, as well as most of Docker code. There is a link for the docker name generator available:  http://frightanic.com/goodies_content/docker-names.php_

