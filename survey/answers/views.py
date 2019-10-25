from django.shortcuts import render
from .models import Answer
from rest_framework import viewsets
from .serializers import AnswerSerializer
# Create your views here.
class AnswerViews(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
