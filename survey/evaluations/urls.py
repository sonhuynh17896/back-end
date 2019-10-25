from rest_framework.routers import DefaultRouter
from .views import EvaluationViews

route = DefaultRouter()
route.register('evaluation', EvaluationViews)

urlpatterns = route.urls