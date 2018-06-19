import autogen.auth_pb2 as auth_pb2
import autogen.auth_pb2_grpc as auth_pb2_grpc
import requests
import os


class Authentication(auth_pb2_grpc.AuthenticationServicer):

    def authenticate(self, request, context):
        # call to the api
        url = os.environ.get('API_URL', 'http://13.231.170.1:8000/')
        username = request.username
        password = request.password
        url = url+'rest-auth/login/'
        r = requests.post(url, data={'username': username, 'password': password})
        # print(r.json())
        g_response = auth_pb2.AuthResponse()
        g_response.status = r.status_code
        if g_response.status == 200:
            g_response.token = r.json().get('key')
        else:
            for i, j in r.json().items():
                error = g_response.errors.add()
                error.field = i
                error.message = j[0] if isinstance(j, list) else j
        return g_response
