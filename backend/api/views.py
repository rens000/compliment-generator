from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ComplimentView(APIView):
    def get(self, request):
        data = {"compliment": "This is a sample compliment!"}
        return Response(data, status=status.HTTP_200_OK)
