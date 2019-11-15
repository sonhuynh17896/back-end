from .models import Answer
from rest_framework import serializers



class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Answer
        fields = ['id']

class AnswersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Answer
        fields = ['id', 'answer', 'isRight']
        


