import datetime
import jwt
from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Password is incorrect')

        payload = {
            'user_id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        serialized_user = UserSerializer(user).data
        return Response({
            'jwt': token,
            'user': serialized_user
        })