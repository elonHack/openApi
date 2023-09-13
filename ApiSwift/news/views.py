from django.shortcuts import render
from .nscrape import nscrape
from rest_framework.generics import ListAPIView
from rest_framework import views, response, status
from .serializers import NewsSerializers
# Create your views here.

data = nscrape.Nscrape('news')

class HomeView(views.APIView):
    def get(self, request):
        return response.Response(data.extract_content(), status=status.HTTP_200_OK)