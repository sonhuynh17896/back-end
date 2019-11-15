from .models import Evaluation
from rest_framework import serializers
from results.serializers import ResultSerializer
from results.models import Result
from answers.models import Answer
from django_filters import rest_framework as filters


class EvaluationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    results = ResultSerializer(many=True)

    class Meta:
        model = Evaluation
        fields = ['id', 'form', 'user', 'submitted_time', 'results']

    def validate(self, data):
        return super().validate(data)

    def create(self, validated_data):
        results = validated_data.pop('results')
        evaluation= Evaluation.objects.create(**validated_data)
        for result in results:
            answers = None
            if result.get('answers'):
                answers = result.pop('answers')
            resultss = Result.objects.create(**result, evaluation=evaluation)
            if answers:
                for answer in answers:
                    answer_id = answer.get('id') 
                    answerss = Answer.objects.get(id = answer_id)
                    answerss.results.add(resultss)
                    answerss.save()
        return evaluation
    

