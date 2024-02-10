from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from.serializers import UserRegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import customUser
from .utils import send_code_to_user


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self,request):
        user_data = request.data
        # print(user_data['password'])
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            send_code_to_user(user['email'])
            return Response({
                'data':user,
                'message':f"hii thanks for signing. you have been registered successfully.",
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            # serializer.save()
            # user = serializer.data
            return Response({
                'data':user_data,
                'message':f"hii you have been logged In successfully.",
            })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

