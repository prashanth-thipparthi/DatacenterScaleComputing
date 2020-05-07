#!/bin/sh

export ip="localhost"
echo "Running test against host $ip"

if [ ! [ping -c 1 $ip ] ];
then
    echo
fi

for img in ../images/*;
do
    echo "Send $img"
    python3 rest-client.py $ip image $img 1
done

sleep 3
echo "Get plates of image with no valid plate"
curl http://localhost:5000/hash/00035fd92ea0bf242d7c3325e1ea9d80
echo ""

sleep 3
echo "Get plates of image with valid plate"
curl http://localhost:5000/hash/e5a38c28141a09b39e8f5976db4e0d16
echo ""

sleep 3
echo "Get hash of known plate"
curl http://localhost:5000/license/T9SJL1
echo ""
