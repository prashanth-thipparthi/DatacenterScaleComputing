from openalpr import Alpr
print("here")
alpr = Alpr('us', '/etc/openalpr/openalpr.conf', '/usr/share/openalpr/runtime_data')

#def recognize_image(filename):
print("here")
results = alpr.recognize_file('car.jpg')
print("here")
if len(results['results']) == 0:
    print("Can't find a plate")
    #return results
else:
    #return results
    print("Most likely plate is", results['results'][0]['plate'])