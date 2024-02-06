from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet


app_name = 'backend'




router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', views.index, name ='indexpage'),
    path('api/', include(router.urls)),
]