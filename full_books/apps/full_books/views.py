from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
	context = {
    "books": Book.objects.all()
  }
	return render(request, 'full_books/index.html', context)

def books(request):
  # using ORM
  Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
  # insert into Book (title, author, category, created_at, updated_at) values (title, blog, now(), now())
  return redirect('/')