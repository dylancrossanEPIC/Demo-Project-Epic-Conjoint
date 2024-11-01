from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def create_course(request):
    return render(request, 'createcourses.html')

def update_course(request):
    return render(request, 'updatecourses.html')