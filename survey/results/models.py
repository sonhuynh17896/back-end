from django.db import models
from answers.models import Answer
from questions.models import Questions
from evaluations.models import Evaluation
# Create your models here.
class Result(models.Model):
    choices = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    value = models.CharField(max_length=150, blank=True, default='', null=True)