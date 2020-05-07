from __future__ import print_function
import requests
import json
import time
import argparse

# prepare headers for http request
def post_image(host, filename):
    addr = "http://"+host+":5000"
    headers = {'content-type': 'image/png'}
    img = open(filename, 'rb').read()
    # send http request with image and receive response
    arr = filename.split('/')
    image_url = addr + '/image/'+arr[len(arr)-1]
    response = requests.put(image_url, data=img, headers=headers)
    # decode response
    print("Response is", response)
    print(response.text)
    #print(json.loads(response.text))

def get_by_checksum(host):
    headers = {'content-type': 'application/json'}
    s = "e5a38c28141a09b39e8f5976db4e0d16"
    url = "http://"+host+":5000"
    url = url+"/hash/"+s
    '''
    body = {'a':num1,
	     'b': num2}
    '''
    #body = json.dumps(body)
    response = requests.get(url, headers=headers)
    # decode response
    print("Response is", response)
    print(json.loads(response.text))

def get_by_licenseplate(host):
    headers = {'content-type': 'application/json'}
    s = "T9SJL1"
    url = "http://"+host+":5000"
    url = url+"/license/"+s
    '''
    body = {'a':num1,
	     'b': num2}
    '''
    #body = json.dumps(body)
    response = requests.get(url, headers=headers)
    # decode response
    print("Response is", response)
    print(json.loads(response.text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    #parser.add_argument('host', help='hostname missing')
    parser.add_argument(
        'image', help='image missing.')
    args = parser.parse_args()
    post_image("localhost", args.image)
    #get_by_checksum("localhost")
    #get_by_licenseplate("localhost")   parser.add_argument('host', help='hostname missing')
