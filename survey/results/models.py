from django.db import models
from questions.models import Questions
from evaluations.models import Evaluation
# Create your models here.
class Result(models.Model):
    
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    value = models.CharField(max_length=150, blank=True, default='', null=True)

    def __str__(self):
        return self.value

    @property
    def answers(self):
        return self.answer_set.all()