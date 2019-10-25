from django.shortcuts import render
from .models import Questions
from rest_framework import viewsets
from .serializers import QuestionSerializer
# Create your views here.
class QuestionViews(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
