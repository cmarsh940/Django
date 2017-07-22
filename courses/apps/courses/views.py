from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

#function to handle the courses
def courses(request):
    if request.method == 'POST':
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(text=request.POST['description'], course_id=course)
    return redirect('/')

#functions to delete page and destroy function 
def delete(request, course_id):
    context = {
        "courses": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/delete.html', context)

def destroy(request, course_id):
    if request.method == 'POST':
        Course.objects.filter(id=course_id).delete()
        return redirect('/')