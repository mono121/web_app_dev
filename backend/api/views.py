from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
# from .ownpermissions import ProfilePermission
# from .serializers import MyTokenObtainPairSerializer 

# class ObtainTokenPairWithColorView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


class UserViweSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (ProfilePermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, IsAuthenticated)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)