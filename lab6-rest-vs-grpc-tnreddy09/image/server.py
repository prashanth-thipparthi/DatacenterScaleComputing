import grpc
from concurrent import futures
import time
import logging
from PIL import Image
import io

import image_pb2
import image_pb2_grpc

def get_dimensions(req):
    ioBuffer = io.BytesIO(req.image)
    img = Image.open(ioBuffer)
    return img

class ImageServiceServicer(image_pb2_grpc.ImageServiceServicer):

    def ImageDimensions(self, request, context):
        img = get_dimensions(request)
        width = img.size[0]
        height = img.size[1]
        return image_pb2.Dimensions(height = height, widht = width)


def image_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageServiceServicer(), server)
    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    image_server()