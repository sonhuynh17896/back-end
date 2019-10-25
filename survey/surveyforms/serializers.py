from .models import SurveyForm
from rest_framework import serializers

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyForm
        fields = ['id','title','description']



class SurveyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyForm
        fields = '__all__'
