from rest_framework import serializers
from django.contrib.auth.models import User

class testSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }
