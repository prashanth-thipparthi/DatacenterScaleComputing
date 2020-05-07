FROM ubuntu:18.04

WORKDIR /app

RUN apt -y update
RUN apt -y install python3 python3-pip
RUN pip3 install Flask \
    jsonpickle \
    numpy

COPY server.py /app/server.py 

CMD ["python3", "server.py"]

EXPOSE 5000
