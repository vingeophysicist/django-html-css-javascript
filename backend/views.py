from django.shortcuts import render
from django.http import JsonResponse
import requests



# Create your views here.
def retrieve_json_data(request, user_type):
    
    student = 'https://my-json-server.typicode.com/depth0/survey1/surveys'
    bachelor = 'https://my-json-server.typicode.com/depth0/survey1/questions'
    
    json_link = student if user_type == 'student' else bachelor
    
    try:
        response = requests.get(json_link)
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
    
    
    

def index(request):
    return render(request, 'index.html')


