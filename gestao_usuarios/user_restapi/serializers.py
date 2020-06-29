from rest_framework import serializers
from user_restapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
          'email', 'name', 'is_staff', 'id',
          'date_joined', 'date_updated', 'date_of_birth'
        ]