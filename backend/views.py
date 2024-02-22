from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Survey, Question
from .serializers import SurveySerializer, QuestionSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView




# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('backend:login')
    template_name = 'register.html'

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    