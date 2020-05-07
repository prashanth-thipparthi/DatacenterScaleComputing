#!/bin/sh
#
version=$1
repo="webserver"
docker build -t $repo:$version .
docker tag $repo:$version gcr.io/join-hadoop/$repo:$version
docker push gcr.io/join-hadoop/$repo:$version
kubectl create deployment $repo --image gcr.io/join-hadoop/$repo:$version
kubectl expose deployment $repo --port 5000 
