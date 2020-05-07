#Download base image ubuntu 16.04
FROM ubuntu:16.04

RUN mkdir /root/.ssh/
COPY /id_rsa /root/.ssh/
COPY /id_rsa.pub /root/.ssh/

RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa.pub

RUN  apt-get -yq update && apt-get -yqq install ssh

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

COPY worker-install.sh /worker-install.sh

COPY test.py /test.py

RUN sh /worker-install.sh

#CMD ["python3", "/test.py"]
CMD ["python3", "/lab8-alpr-kubernetes-tnreddy09/worker/worker.py"]