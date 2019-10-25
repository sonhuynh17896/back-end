from rest_framework.routers import DefaultRouter
from .views import SurveyFormViews

route = DefaultRouter()
route.register('form', SurveyFormViews)

urlpatterns = route.urls