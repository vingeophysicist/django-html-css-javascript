from django.shortcuts import render
from rest_framework import viewsets
from .models import Survey, Question
from .serializers import SurveySerializer, QuestionSerializer



# Create your views here.


def index(request):
    return render(request, 'index.html')

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer