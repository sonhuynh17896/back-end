from django.shortcuts import render
from .models import Result
from rest_framework import viewsets
from .serializers import ResultSerializer
# Create your views here.
class ResultViews(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
