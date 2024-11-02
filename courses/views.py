from django.shortcuts import render
from django.http import HttpRequest
import requests
import json

def index(request):
    response = requests.get('http://127.0.0.1:8000/api/courses')
    courses = response.json()
    return render(request, 'index.html',{'courses':courses})

def create_course(request):
    return render(request, 'createcourses.html')

def update_course(request):
    return render(request, 'updatecourses.html')