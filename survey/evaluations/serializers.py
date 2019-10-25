from .models import Evaluation
from rest_framework import serializers

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
