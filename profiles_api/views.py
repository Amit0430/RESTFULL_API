from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """ Return a list of features of APIView"""
        an_apiView = [
        'Used HTTP functions (get, post, pathch, put, delete) ',
        'Is similer to traditional Django views',
        'Gives you the most control over application',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})
