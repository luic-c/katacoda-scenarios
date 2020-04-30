FROM ubuntu:latest
COPY ./request.py /deploy/
COPY ./model.pkl /deploy/
WORKDIR /deploy/
RUN apt-get update \  
  && apt-get install -y python3-pip python3-dev \  
  && cd /usr/local/bin \  
  && ln -s /usr/bin/python3 python \  
  && pip3 install flask sklearn pandas seaborn matplotlib
EXPOSE 80
ENTRYPOINT ["python3", "request.py"]