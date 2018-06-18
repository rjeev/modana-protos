import time
import grpc
import os
import autogen.auth_pb2_grpc as auth_pb2_grpc
from services.autheticate import Authentication
from concurrent import futures
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthenticationServicer_to_server(Authentication(), server)
    server.add_insecure_port('0.0.0.0:{}'.format(os.environ['PORT']))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
