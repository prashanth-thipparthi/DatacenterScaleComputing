import grpc

import AddNumbers_pb2
import AddNumbers_pb2_grpc

channel = grpc.insecure_channel('localhost:50052')

stub = AddNumbers_pb2_grpc.AddNumbersStub(channel)

input = AddNumbers_pb2.input(a=5,b=6)

response = stub.AddNumbers(input)

print(response.value)