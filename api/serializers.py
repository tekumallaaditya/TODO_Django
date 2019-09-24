from rest_framework import serializers

class testSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)