#!/bin/bash
sudo docker build -t jdtotow/flask:latest . -f ./deployment/Dockerfile
sudo docker push jdtotow/flask:latest
