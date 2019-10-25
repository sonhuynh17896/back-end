from django.shortcuts import render
from .models import Evaluation
from rest_framework import viewsets
from .serializers import EvaluationSerializer
# Create your views here.
class EvaluationViews(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
