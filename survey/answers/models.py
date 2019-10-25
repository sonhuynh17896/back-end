from django.db import models
from questions.models import Questions
# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=250)
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    isRight = models.BooleanField(default=False)