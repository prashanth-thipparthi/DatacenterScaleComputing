from openalpr import Alpr

def getplate(filename):
    alpr = Alpr('us', '/etc/openalpr/openalpr.conf', '/usr/share/openalpr/runtime_data')
    results = alpr.recognize_file(filename)
    return results
