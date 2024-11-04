from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests
import json
from .forms import CreateCourseForm, UpdateCourseForm

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
    return render(request, 'createcourse.html',{"form":form})

def update_course(request, id):
    course_id = str(id)
    if request.method == "POST":
        form = UpdateCourseForm(request.POST)
        print(json.dumps(form.data))
        course = {
            "id":course_id,
            "course_title" :form.data['course_title'],
            "course_details" :form.data['course_details'],
            "course_pub_date" :form.data['course_pub_date']
        }
        requests.put('http://127.0.0.1:8000/api/courses/'+ course_id, json.dumps(course))
        return redirect("http://127.0.0.1:8000")
    else:
        response = requests.get('http://127.0.0.1:8000/api/courses/'+ course_id)
        dict = json.loads(response.content)
        form = UpdateCourseForm(initial=dict)
        return render(request, 'updatecourse.html',{"form":form})



def delete_course(request, id):
    course_id = str(id)
    requests.delete('http://127.0.0.1:8000/api/courses/'+ course_id)
    print(course_id)
    return redirect("http://127.0.0.1:8000")

