FROM ubuntu:16.04 
RUN apt-get update
RUN apt-get install -y python3
RUN mkdir /script 
COPY lab2.py /script  
ENTRYPOINT [ "python", "/script/lab2.py" ]
