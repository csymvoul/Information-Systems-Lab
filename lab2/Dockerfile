<<<<<<< HEAD
FROM ubuntu:16.04 
RUN apt-get update
RUN apt-get install -y python3
RUN mkdir /script 
COPY lab2.py /script  
ENTRYPOINT [ "python", "/script/lab2.py" ]
=======
FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3
RUN mkdir /lab2
COPY lab2.py /lab2
ENTRYPOINT ["python3","-u","/lab2/lab2.py"]
>>>>>>> aef302b207ffd515094192f239229c20e97d62f5
