from django_filters import rest_framework as filters
from .models import Evaluation

class EvaluationFilter(filters.FilterSet):
    form = filters.CharFilter(field_name='form__id')
    user = filters.CharFilter(field_name='user__id')
    class Meta:
        model = Evaluation
        fields = ['form', 'user']

   
            