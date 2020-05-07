import grpc
from concurrent import futures
import time
import logging

import AddNumbers_pb2
import AddNumbers_pb2_grpc

def add_numbers(a, b):
    c = a+b
    print("c:",c)
    return c

class AddNumbersServicer(AddNumbers_pb2_grpc.AddNumbersServicer):

    def AddNumbers(self, request, context):
        response = AddNumbers_pb2.Number()
        response.value = add_numbers(request.a, request.b)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

AddNumbers_pb2_grpc.add_AddNumbersServicer_to_server(AddNumbersServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()
server.wait_for_termination()
