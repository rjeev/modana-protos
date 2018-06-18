# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import autogen.auth_pb2 as auth__pb2


class AuthenticationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.autheticate = channel.unary_unary(
        '/Authentication/autheticate',
        request_serializer=auth__pb2.AuthRequest.SerializeToString,
        response_deserializer=auth__pb2.AuthResponse.FromString,
        )


class AuthenticationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def autheticate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthenticationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'autheticate': grpc.unary_unary_rpc_method_handler(
          servicer.autheticate,
          request_deserializer=auth__pb2.AuthRequest.FromString,
          response_serializer=auth__pb2.AuthResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Authentication', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
