FROM ubuntu:latest
COPY ./request.py /deploy/
COPY ./model.pkl /deploy/
WORKDIR /deploy/
RUN pip install flask sklearn pandas seaborn matplotlib
EXPOSE 80
ENTRYPOINT ["python3", "request.py"]