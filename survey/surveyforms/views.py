from django.shortcuts import render
from .models import SurveyForm
from rest_framework import viewsets
from .serializers import SurveyFormSerializer
# Create your views here.
class SurveyFormViews(viewsets.ModelViewSet):
    queryset = SurveyForm.objects.all()
    serializer_class = SurveyFormSerializer
