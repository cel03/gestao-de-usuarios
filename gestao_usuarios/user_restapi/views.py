from rest_framework import viewsets
from rest_framework import permissions
from user_restapi.models import User
from user_restapi.serializers import UserSerializer
#from user_restapi.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly]