#FROM ubuntu:16.04
FROM python:3.7 
#RUN apt-get update 
#RUN apt-get install -y python3 python3-pip 
RUN pip install requests 
RUN mkdir /app 
COPY ex2.py /app 
CMD ["python","-u","/app/ex2.py"]