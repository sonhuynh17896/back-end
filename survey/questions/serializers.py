from .models import Questions
from surveyforms.models import SurveyForm
from rest_framework import serializers
from surveyforms.serializers import FormSerializer
from rest_framework.relations import PrimaryKeyRelatedField


class ModelRepresentationPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.model_serializer_class = kwargs.pop('model_serializer_class')
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        print(type(self.model_serializer_class(instance=value).data))
        return self.model_serializer_class(instance=value).data

class QuestionSerializer(serializers.ModelSerializer):
    form = ModelRepresentationPrimaryKeyRelatedField(queryset=SurveyForm.objects.all(), model_serializer_class=FormSerializer)
    
    class Meta:
        model = Questions
        fields = '__all__'
        
