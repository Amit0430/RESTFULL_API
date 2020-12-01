from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of features of APIView"""
        an_apiView = [
        'Used HTTP functions (get, post, pathch, put, delete) ',
        'Is similer to traditional Django views',
        'Gives you the most control over application',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        """ Create a Hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handling updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle parial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Handle delete an object """
        return Response({'method': 'DELETE'})
