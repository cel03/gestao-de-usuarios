from rest_framework import serializers
from user_restapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
          'id', 'email', 'name', 'is_staff',
          'date_joined', 'date_updated', 'date_of_birth'
        ]