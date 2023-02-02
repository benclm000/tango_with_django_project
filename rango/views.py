from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Go to the about page with http://127.0.0.1:8000/rango/about")
    
def about(request):
    return HttpResponse("Rango says here is the about page. Go back to the main page with http://127.0.0.1:8000/rango/")
