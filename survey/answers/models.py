from django.db import models
from questions.models import Questions
from django.db.models import Q
from results.models import Result
# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=250)
    question = models.ForeignKey(Questions, on_delete= models.CASCADE, limit_choices_to=~Q(type_questions ='text'))
    isRight = models.BooleanField(default=False)
    results = models.ManyToManyField(Result, null=True, blank=True)
    def __str__(self):
        return self.answer