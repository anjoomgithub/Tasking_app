# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # Add is_staff to the serializer
        fields = ('id', 'username', 'email', 'password', 'points', 'profile_picture', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('is_staff',) # Make is_staff read-only

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user