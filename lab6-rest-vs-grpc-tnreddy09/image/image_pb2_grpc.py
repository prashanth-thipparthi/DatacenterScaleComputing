# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import image_pb2 as image__pb2


class ImageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ImageDimensions = channel.unary_unary(
        '/ImageService/ImageDimensions',
        request_serializer=image__pb2.Image.SerializeToString,
        response_deserializer=image__pb2.Dimensions.FromString,
        )


class ImageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ImageDimensions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ImageDimensions': grpc.unary_unary_rpc_method_handler(
          servicer.ImageDimensions,
          request_deserializer=image__pb2.Image.FromString,
          response_serializer=image__pb2.Dimensions.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ImageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))