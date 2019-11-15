from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SurveyForm(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('private', 'Private'),
        ('public', 'Public'),
        ('close', 'Close')
    ]
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)
    requireLoggedIn = models.BooleanField(default=False)
    maxTimeEvaluation = models.IntegerField(default=0)
    starttime_evaluation = models.DateTimeField(null=True, blank=True)
    endtime_evaluation = models.DateTimeField(null=True, blank=True)
    limitNumberofEvaluation  = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='open')
    key = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.title

    @property
    def questions(self):
        return self.questions_set.all()


    