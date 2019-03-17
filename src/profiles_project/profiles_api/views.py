from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your  views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format = None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as a function (Get, Post, patch, put, delete)',
            'It si similar to a traditional Django view',
            'Gives youthe most control over your logic',
            'IS mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
