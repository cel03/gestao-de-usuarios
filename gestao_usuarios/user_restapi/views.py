from rest_framework import viewsets
from rest_framework import permissions
from user_restapi.models import User
from user_restapi.serializers import UserSerializer
from user_restapi.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#class UserDetails(generics.RetrieveUpdateDestroyAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly]

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import authentication, permissions
#from user_restapi.models import User

#class ListUsers(APIView):
#    """
#    View to list all users in the system.

#    * Requires token authentication.
#    * Only admin users are able to access this view.
#    """
#    authentication_classes = [authentication.TokenAuthentication]
#    permission_classes = [permissions.IsAdminUser]

#    def get(self, request, format=None):
#        """
#        Return a list of all users.
#        """
#        usernames = [user.username for user in User.objects.all()]
#        return Response(usernames)

#class UserDetails(APIView):
#
#    def get_object(self, pk):
#        try:
#            return User.objects.get(pk=pk)
#        except User.DoesNotExist:
#            raise Http404
#        
#    def get(self, request, pk):
#        user = self.get_object(pk)
#        serializer = UserSerializer(user)
#        return Response(serializer.data)
#    
#    def put(self, request, pk):
#        user = self.get_object(pk)
#        serializer = UserSerializer(user, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#    
#    def delete(self, request, pk):
#        user = self.get_object(pk)
#        user.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
