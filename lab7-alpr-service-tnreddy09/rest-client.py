from __future__ import print_function
import requests
import json
import time

addr = 'http://localhost:5000'

# prepare headers for http request
def post_image():
    headers = {'content-type': 'image/png'}
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    # send http request with image and receive response
    image_url = addr + '/api/image'
    response = requests.post(image_url, data=img, headers=headers)
    # decode response
    print("Response is", response)
    print(json.loads(response.text))

def get_sum():
    num1 = 5
    num2 = 9
    headers = {'content-type': 'application/json'}
    url = addr+'/api/add/'+str(num1)+'/'+str(num2)
    '''
    body = {'a':num1,
	     'b': num2}
    '''
    #body = json.dumps(body)
    response = requests.get(url, headers=headers)
    # decode response
    print("Response is", response)
    print(json.loads(response.text))

start_time = time.time()
for(i in range(1000):
    #get_sum()
    post_image()
print("time:",time.time()-start_time)
