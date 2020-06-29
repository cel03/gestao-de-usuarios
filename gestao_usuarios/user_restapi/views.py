from rest_framework import viewsets
from rest_framework import permissions
from user_restapi.models import User
from user_restapi.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer