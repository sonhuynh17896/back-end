from django_filters import rest_framework as filters
from .models import SurveyForm

class FormFilter(filters.FilterSet):
    questions = filters.CharFilter(field_name='questions_id')
    
    class Meta:
        model = SurveyForm
        fields = ['questions']

   
            