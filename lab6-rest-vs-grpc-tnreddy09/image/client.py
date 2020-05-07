import grpc

import image_pb2
import image_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = image_pb2_grpc.ImageServiceStub(channel)

image = image_pb2.Image(image = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read())

response = stub.ImageDimensions(image)

print(response.height)
print(response.widht)
