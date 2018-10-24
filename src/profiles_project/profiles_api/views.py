from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            "Uses HTTP methods as functions (GET, POST, PUT, PATCH & DELETE)",
            "It is similar to a traditional Django View",
            "It gives you most control over your logic",
            "Is mapped manually to URL's"
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

