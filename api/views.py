from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api import serializers

from .models import todomodel

class todoviews(APIView):
    """todo API view"""
    serializer_class = serializers.testSerializer

    def get(self, request):
        """Returns a list of todo items"""
        return Response({'hello': 'Aditya', 'wife': 'Deepika'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response({'hello': serializer.validated_data.get('name')})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})

