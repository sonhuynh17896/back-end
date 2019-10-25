from rest_framework.routers import DefaultRouter
from .views import QuestionViews

route = DefaultRouter()
route.register('questions', QuestionViews)

urlpatterns = route.urls