from django.db import models
from surveyforms.models import SurveyForm
# Create your models here.
class Questions(models.Model):
    TYPE_QUESTION = [
        ('text', 'Text'),
        ('selection', 'Selection'),
        ('multiple', 'Multiple')
    ]
    title = models.CharField(max_length=250)
    type_questions = models.CharField(max_length=20, choices=TYPE_QUESTION, default='text')
    isRequired = models.BooleanField(default=False)
    form = models.ForeignKey(SurveyForm, on_delete=models.CASCADE)

    def __str__(self):
        return self.title