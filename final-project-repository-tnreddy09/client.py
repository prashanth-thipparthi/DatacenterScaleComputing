import grequests
import json
import sys
#from time import perf_counter 
import time

def mul(ip, x, n_iter):
    requests = []
    url = "{0}mul/{1}/{2}".format(ip, x, x)
    for i in range(n_iter):
        requests.append(grequests.get(url))
    print("Sending Requests")
    grequests.map(requests)

def attack(api, n_iter):
    url = None
    if api == 'protected' or api == 'frontend':
        url = 'http://34.83.176.120'
    elif api == 'unprotected':
        url = 'http://35.238.191.49'
    elif api == 'backend':
        url = 'http://34.83.127.198/toxicity?text=hello'
    if url is None:
        print("please enter correct api (backend/frontend)")
    else:
        requests = []
        for i in range(n_iter):
            requests.append(grequests.get(url))
        print("Sending Requests")
        print(grequests.map(requests))
    print("Attack Complete!!")

if __name__ == "__main__":
    api = sys.argv[1]
    n_iter = int(sys.argv[2])
    x = 1
    if len(sys.argv) > 3:
        x = int(sys.argv[3])
    ip = "http://34.82.145.163/"
    if api == 'protected' or api == 'frontend':
        attack(api, n_iter)
    elif api == 'unprotected':
        attack(api, n_iter)
    elif api == 'backend':
        attack(api, n_iter)
    elif api == 'multiply':
        mul(ip, x, n_iter)
