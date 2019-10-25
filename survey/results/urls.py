from rest_framework.routers import DefaultRouter
from .views import ResultViews

route = DefaultRouter()
route.register('result', ResultViews)

urlpatterns = route.urls