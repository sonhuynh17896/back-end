from .models import Result
from rest_framework import serializers
from questions.serializers import QuestionsSerializer
from answers.serializers import AnswerSerializer
from questions.models import Questions

class ResultSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    answers = AnswerSerializer(many=True, required=False)

    def validate(self, data):
        # super().validate(data)
        answer = data.get('answers')
        value = data.get('value')
        question = data.get('question')
        if self.instance:
            question = self.instance.question
        else:
            type_question = question.type_questions
            if type_question == 'text':
                if not value:
                    raise serializers.ValidationError({'value': ["value must not be null "]})
                else:
                    if answer:
                        raise serializers.ValidationError({'answer': ["no answer"]})
            else:
                if value:
                    raise serializers.ValidationError({'value': ["no value "]})
                else:
                    if not answer:
                        raise serializers.ValidationError({'answer': ["answer must not be null"]})
                if type_question == 'yes/no':
                    if answer == 1:
                        raise serializers.ValidationError({'answer':["need one answer"]})
                if type_question == 'multiple':
                    if not answer:
                        raise serializers.ValidationError({'answer':["need many answer"]})
                
        return data

    class Meta:
        model = Result
        fields = ['id', 'answers', 'question', 'value']

