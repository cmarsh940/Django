from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Course
# Create your views here.
def index(request):
	context = {
	 'courses' : Course.objects.all()
	}
	return render(request, 'courses/index.html', context)

def courses(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def action(request):
	return render(request, 'courses/action.html')

def course_delete(request, id):
    course = Course.objects.all(course, id=id)
    course.delete()
    return redirect('get:index')