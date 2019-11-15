from django.shortcuts import render
from .models import Questions
from rest_framework import viewsets
from .serializers import QuestionsSerializer
# Create your views here.
class QuestionViews(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
