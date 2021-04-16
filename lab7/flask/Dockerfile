FROM ubuntu:16.04 
MAINTAINER JD TOTOW <totow@unipi.gr>
RUN apt-get update
RUN apt-get install -y python3 python3-pip 
RUN pip3 install --upgrade pip
RUN pip3 install flask pymongo prometheus_client psutil requests
RUN mkdir /app
RUN mkdir -p /app/data
COPY src/service.py /app/service.py  
COPY src/prom.py /app/prom.py 
COPY src/mon.py /app/mon.py 
COPY src/metricsender.py /app/metricsender.py 
ADD src/data /app/data 
EXPOSE 5000
WORKDIR /app
ENTRYPOINT [ "python3","-u", "service.py" ]
