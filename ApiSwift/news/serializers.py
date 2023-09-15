from rest_framework.serializers import ModelSerializer
from .models import News
from rest_framework import serializers

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        exclude = ['id']