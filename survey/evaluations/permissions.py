
from rest_framework import permissions
from surveyforms.models import SurveyForm
from surveyforms.permissions import FormPermission
class EvaluationPermission(permissions.BasePermission):
   
    def has_permission(self, request, view):
        id_form = request.data.get('form')
        form = SurveyForm.objects.get(id=id_form)
        return FormPermission().has_object_permission(request, view, form)
       
    
 

        

