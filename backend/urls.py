from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet


app_name = 'backend'




router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey_list')
router.register(r'surveys/<int:id>/', SurveyViewSet, basename='survey_details' )
router.register(r'questions', QuestionViewSet, basename='question_list')
router.register(r'questions/<int:id>/', QuestionViewSet, basename='question_details')



urlpatterns = [
    path('', views.index, name ='indexpage'),
    path('api/', include(router.urls)),
]