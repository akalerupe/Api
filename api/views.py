from django.shortcuts import render

from .serializers import HeroSerializer
from .models import Hero
from rest_framework.views import APIView

class HeroViewSet(APIView):
    queryset=Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

