from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests
import json
from .forms import CreateCourseForm

def index(request):
    response = requests.get('http://127.0.0.1:8000/api/courses')
    courses = response.json()
    
    return render(request, 'index.html',{'courses':courses})

def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        # print(json.dumps(form.data))
        course = {
            "course_title" :form.data['course_title'],
            "course_details" :form.data['course_details'],
            "course_pub_date" :form.data['course_pub_date']
        }
        print(course)
        print(json.dumps(course))


        requests.post('http://127.0.0.1:8000/api/courses', json.dumps(course))
        return redirect("http://127.0.0.1:8000")
        

    else:
        form = CreateCourseForm()
    return render(request, 'createcourses.html',{"form":form})

def update_course(request):
    return render(request, 'updatecourse.html')

def delete_course(request, id):
    course_id = str(id)
    requests.delete('http://127.0.0.1:8000/api/courses/'+ course_id)
    print(course_id)
    return redirect("http://127.0.0.1:8000")

