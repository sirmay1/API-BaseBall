from django.shortcuts import render
from rest_framework import viewsets
from .models import Baseball
from .serializers import BaseballSerializer

class BaseballView(viewsets.ModelViewSet):
    queryset = Baseball.objects.all()
    serializer_class = BaseballSerializer
    
    
    
    
    
