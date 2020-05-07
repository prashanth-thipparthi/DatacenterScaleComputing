FROM ubuntu:18.04

WORKDIR /app

RUN apt -y update
RUN apt -y install python3 python3-pip
RUN pip3 install Flask \
    jsonpickle \
    numpy \
    requests

COPY blacklist_unblacklist.py /app/blacklist_unblacklist.py 

CMD ["python3", "blacklist_unblacklist.py"]

EXPOSE 5001
