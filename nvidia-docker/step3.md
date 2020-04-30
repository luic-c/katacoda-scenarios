Now that we have an application ready to be containerized, we need to write a Dockerfile to build an image.

## Dockerize

The Dockerfile is a list of commands that the user needed to execute in order to generate the image, i.e. setting up the environment or even running the program.

`touch Dockerfile  `{{execute}}

Here we first specify the base image to work on (`ubuntu:latest`), then run `apt-get` and `pip install` to get python3 and necessary packages. We also expose port 80 to outside of the container for our flask app to use. Finally, the Entrypoint specifies the main command to run.

Copy and paste the code below to Dockerfile

<pre class="file" data-target="clipboard">
FROM ubuntu:latest
RUN apt-get update \  
  && apt-get install -y python3-pip python3-dev \  
  && cd /usr/local/bin \  
  && ln -s /usr/bin/python3 python \  
  && pip3 install Flask sklearn pandas seaborn matplotlib
EXPOSE 80
ENTRYPOINT ["python3", "app.py"]
</pre>



Build the docker image `iris_app` required by running the command:

`docker build --tag iris_app . `{{execute}}

To run the image as container, run the following command to start the terminal in the container:

`docker run -p 5000:80 -it iris_app /bin/bash  `{{execute}}

> Note: If you give the client Dockerfile, they can just build the container and run it without needing to manually run pip install themselves

To exit the container terminal, we simply type:

`exit  `{{execute}}

To check whether the container is running, run the command:

`docker container ls  `{{execute}}

The terminal will show that the container is running and up for (...) minutes.



> _Fun Fact: Notice that there is also a NAMES column besides Container ID. It can be used interchangeably as the ID as it is more readable to human. The name generator is actually written in Go, as well as most of Docker code. There is a link for the docker name generator available:  http://frightanic.com/goodies_content/docker-names.php_