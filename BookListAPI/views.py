from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView

@api_view(['POST'])
def books(request):
    return Response('List of the books', status=status.HTTP_200_OK)


@api_view(['POST'])
def tests(request):
    return Response('Test', status=status.HTTP_200_OK)

# Create your views here.

class BookList(APIView):
    def get(self, request):
        return Response({'Message':'List of the books'}, status.HTTP_200_OK)