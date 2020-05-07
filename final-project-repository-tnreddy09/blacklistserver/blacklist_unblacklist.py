from flask import Flask, request, Response
import requests
import json
import sys
#from time import perf_counter 
import jsonpickle
import time

app = Flask(__name__)

hostname_ip_map = {
    'webserver-dsc': 'http://34.83.176.120/',
    'bert-dsc': 'http://34.83.236.119/'
}
def getInfo(server_ip, ip):
    url = "{0}api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "1" 
    }
    headers = {'content-type': 'application/json'}
    response = requests.get(url, data=json.dumps(data), headers=headers)
    status = "unknown"
    value = response.json().get(ip) 
    if value is not None:
        if value == "1":
            status = "blacklist"
        else:
            status = "Non Blacklisted"

    print("current status - {0}".format(status))
    return response.json().get(ip)

@app.route('/block', methods=['POST'])
def blockIP():
    print('Data Received - {0}'.format(request.json))
    ip = request.json.get('ip')
    hostname = request.json.get('hostname')
    server_ip = ""
    if hostname is not None and hostname_ip_map.get(hostname):
        server_ip = hostname_ip_map.get(hostname)
    else:
        print("hostname not configured")
    url = "{0}api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "1" 
    }
    headers = {'content-type': 'application/json'}
    method = 'post'
    response_pickled = jsonpickle.encode({
        'text': 'error' 
    })
    try:
        is_existing = getInfo(server_ip, ip)
        if is_existing:
            method = 'patch'
        response = requests.request(method, url, data=json.dumps(data), headers=headers)
        response_pickled = jsonpickle.encode({
            'text': 'blocked' 
        })
    except Exception as e:
        print(e)
        print('data - {0}'.format(request.json))
    return Response(response=response_pickled, status=200)

@app.route('/unblock', methods=['POST'])
def unblockIP():
    print('Data Received - {0}'.format(request.json))
    ip = request.json.get('ip')
    hostname = request.json.get('hostname')
    server_ip = ""
    if hostname is not None and hostname_ip_map.get(hostname):
        server_ip = hostname_ip_map.get(hostname)
    else:
        print("hostname not configured")
    url = "{0}api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "0"
    }
    headers = {'content-type': 'application/json'}
    method = 'post'
    response_pickled = jsonpickle.encode({
        'text': 'error' 
    })
    try:
        is_existing = getInfo(server_ip, ip)
        if is_existing:
            method = 'patch'
        response = requests.request(method, url, data=json.dumps(data), headers=headers)
        response_pickled = jsonpickle.encode({
            'text': 'unblocked' 
        })
    except Exception as e:
        print(e)
        print('data - {0}'.format(request.json))
    return Response(response=response_pickled, status=200)

app.run(host="0.0.0.0", port=5001)

#if __name__ == "__main__":
#    server_ip="localhost"
#    ip = sys.argv[1]
#    api = sys.argv[2]
#    if api == 'block':
#        blockIP(server_ip, ip)
#    elif api == 'unblock':
#        unblockIP(server_ip, ip)
#    elif api == 'getinfo':
#        getInfo(server_ip, ip)
