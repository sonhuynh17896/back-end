from django.shortcuts import render
from .models import SurveyForm
from rest_framework import viewsets, permissions
from .serializers import SurveyFormSerializer
from rest_framework.response import Response
from .permissions import FormPermission
from django_filters import rest_framework as filters
from .filters import FormFilter
# Create your views here.
class SurveyFormViews(viewsets.ModelViewSet):
    queryset = SurveyForm.objects.all()
    serializer_class = SurveyFormSerializer
    permission_classes = (FormPermission,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = FormFilter
    


    

    