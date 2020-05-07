from flask import Flask, request, Response
import jsonpickle
import numpy as np
import io

# Initialize the Flask application
app = Flask(__name__)

@app.route('/mul/<int:X>/<int:Y>', methods=['GET'])
def add(X, Y):
    a = np.random.rand(X,Y)
    b = np.linalg.inv(a)
    c = np.mean(np.dot(a,b))
    response = {
        'sum': float(c) 
    }
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
        return 'You want path: %s' % path
    
# route http posts to this method
app.run(host="0.0.0.0", port=5000)

