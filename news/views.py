from django.shortcuts import render
from .models import Story
from rest_framework.views import APIView
from.serializer import StorySerializer
from rest_framework.response import Response
# Create your views here.

class StoryView(APIView):
    def get(self, request):
        news = Story.objects.all()
        serializer = StorySerializer(news, many=True)
        return Response(serializer.data)
