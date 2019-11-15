from .models import SurveyForm
from rest_framework import serializers
from questions.serializers import QuestionsSerializer
from .models import SurveyForm
from django.contrib.auth.models import User
from questions.models import Questions
from answers.models import Answer

# class CustomCurrentUserDefault(serializers.CurrentUserDefault):
#     def set_context(self, serializer_field):
#         self.user = User.objects.get(id=serializer_field.context['request'].user.id)

class SurveyFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    questions = QuestionsSerializer(many=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('created_by').read_only = True
            self.fields.get('created_time').read_only = True


    class Meta:
        model = SurveyForm
        fields = ['id', 'title', 'description', 'created_time', 'modified_time', 'created_by', 'requireLoggedIn', 'maxTimeEvaluation', 'starttime_evaluation', 'endtime_evaluation', 'limitNumberofEvaluation', 'status', 'key', 'questions']
        # extra_kwargs = {
        #     'created_by': {'default': CustomCurrentUserDefault() },
        #     'modified_by': {'default': CustomCurrentUserDefault() }
        # }

    def validate(self, data):
         return super().validate(data)
        

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        form = SurveyForm.objects.create(**validated_data)
        for question in questions:
            answers = question.pop('answers')
            questionss = Questions.objects.create(**question, form=form)
            for answer in answers:
                Answer.objects.create(**answer, question=questionss)
        return form


    def update(self, instance, validated_data):
        questions = validated_data.pop('questions')
        
        super().update(instance, validated_data)
        keep_questions = []
        for question in questions:
            answers = question.pop('answers')
            if "id" in question.keys():
                if Questions.objects.filter(id=question["id"]).exists():
                    q = Questions.objects.get(id=question["id"])
                    q.title = question.get('title', q.title)
                    q.save()
                    keep_questions.append(q.id)
            else:
                q = Questions.objects.create(**question, form=instance)
                keep_questions.append(q.id)

            keep_answers = []
            for answer in answers:
                if "id" in answer.keys():
                    if Answer.objects.filter(id=answer["id"]).exists():
                        a = Answer.objects.get(id=answer["id"])
                        a.answer = answer.get('answer', a.answer)
                        a.save()
                        keep_answers.append(a.id)
                    
                else:
                    a = Answer.objects.create(**answer, question_id=keep_questions[-1:][0])
                    keep_answers.append(a.id)
        for question in instance.questions:
            if question.id not in keep_questions:
                question.delete()
            for answer in question.answers:
                if answer.id not in keep_answers:
                    answer.delete()            
        
        return instance
                    