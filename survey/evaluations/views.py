from django.shortcuts import render
from .models import Evaluation
from rest_framework import viewsets
from .serializers import EvaluationSerializer
from django_filters import rest_framework as filters
from .filters import EvaluationFilter
from .permissions import EvaluationPermission
# Create your views here.
class EvaluationViews(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EvaluationFilter
    permission_classes = (EvaluationPermission,)
    
    


        

    
            
    

   
            
    
    
