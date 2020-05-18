import json
import logging
from django.contrib.auth import get_user_model                                                                                                                    from django.db import models
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
import rest_framework.status
from .authentication import token_expire_handler, expires_in
from .serializers import *

User = get_user_model()

class SignUpAPI(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user = user)
        is_expired, token = token_expire_handler(token)
        return Response({"expires_in": expires_in(token),
                         "token": token.key},
                        status=status.HTTP_201_CREATED)

# here we specify permission by default we set IsAuthenticated
class SignInAPI(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username = serializer.data['username'],
            password = serializer.data['password'] 
        )
        if not user:
            return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)
        
        #TOKEN STUFF
        token, _ = Token.objects.get_or_create(user = user)
    
        #token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)     # The implementation will be described further
        user_serialized = UserSerializer(user)

        return Response({'expires_in': expires_in(token),
                         'token': token.key},
                        status=status.HTTP_200_OK)


class SignOutAPI(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignOutSerializer
    
    def post(self, request):
        info("Sign out")
        serializer = self.get_serializer(data = request.data)
        if not serializer.is_valid():
            return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username = serializer.data['username'],
            password = serializer.data['password'] 
        )
        if not user:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get(user = user)
        token.delete()
        return Response("Sign out", status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET"])
# def user_info(request):
#     return Response({
#         'user': request.user.username,
#         'expires_in': expires_in(request.auth)
#     }, status=HTTP_200_OK)

            
def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)


