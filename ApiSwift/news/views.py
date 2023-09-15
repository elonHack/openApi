from django.shortcuts import render
from typing import Optional
from .models import News
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import views, response, status
from .serializers import NewsSerializer
from rest_framework import permissions, throttling, decorators,authentication
# Create your views here.

class ViewThrothilng(throttling.SimpleRateThrottle):
    rate = '1/day'

class HomeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request, category=None):
        # param = int(request.query_params.get('limit'))
        news = News.objects.all().order_by("?")
        if category:
            news = News.objects.filter(category=category).order_by("?")
        serialzer = NewsSerializer(news, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)