from django.db import models
from surveyforms.models import SurveyForm
from django.contrib.auth.models import User
# Create your models here.
class Evaluation(models.Model):
    form = models.ForeignKey(SurveyForm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    submitted_time = models.DateTimeField(auto_now_add=True)

