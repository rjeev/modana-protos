import autogen.auth_pb2 as auth_pb2
import autogen.auth_pb2_grpc as auth_pb2_grpc


class Authentication(auth_pb2_grpc.AuthenticationServicer):

    def authenticate(self, request, context):
        return auth_pb2.AuthResponse(status='ok', token='this is a token')