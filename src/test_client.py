from __future__ import print_function

import grpc
import os
import autogen.auth_pb2 as auth_pb2
import autogen.auth_pb2_grpc as auth_pb2_grpc


def run():
    channel = grpc.insecure_channel('0.0.0.0:{}'.format(os.environ['PORT']))
    stub = auth_pb2_grpc.AuthenticationStub(channel)
    response = stub.authenticate(auth_pb2.AuthRequest(username='test', password='test'))
    print(response.status, response.token)


if __name__ == '__main__':
    run()