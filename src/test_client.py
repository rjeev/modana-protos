from __future__ import print_function

import grpc
import os
import autogen.auth_pb2 as auth_pb2
import autogen.auth_pb2_grpc as auth_pb2_grpc


def run():
    channel = grpc.insecure_channel('13.231.170.1:{}'.format(os.environ.get('PORT', '5000')))
    # channel = grpc.insecure_channel('0.0.0.0:{}'.format(os.environ.get('PORT', '5000')))
    stub = auth_pb2_grpc.AuthenticationStub(channel)
    response = stub.authenticate(auth_pb2.AuthRequest(username='admin1234', password='test123'))
    print(response)
    # print(response.status, response.token)
    # for error in response.errors:
    #     print(error.field)
    #     print(error.message)


if __name__ == '__main__':
    run()