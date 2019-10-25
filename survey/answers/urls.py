from rest_framework.routers import DefaultRouter
from .views import AnswerViews

route = DefaultRouter()
route.register('answer', AnswerViews)

urlpatterns = route.urls