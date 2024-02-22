from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet
from django.contrib.auth import views as auth_views
from .views import CustomRegisterView




app_name = 'backend'




router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey_list')
router.register(r'surveys/<int:id>/', SurveyViewSet, basename='survey_details' )
router.register(r'questions', QuestionViewSet, basename='question_list')
router.register(r'questions/<int:id>/', QuestionViewSet, basename='question_details')



urlpatterns = [
    path('', views.index, name ='indexpage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', CustomRegisterView.as_view(template_name='register.html'), name='register'),
    path('api/', include(router.urls)),
    
]