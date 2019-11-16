
from rest_framework import permissions
from surveyforms.models import SurveyForm
from surveyforms.permissions import FormPermission
class EvaluationPermission(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if view.action == 'create':
            id_form = request.data.get('form')
            form = SurveyForm.objects.get(id=id_form)
            if form:
                return FormPermission().has_object_permission(request, view, form)
            return False
        return True
       
    
 

        

