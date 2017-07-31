from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book, Review
from ..login_register.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect

# Create your views here.

#main page to display all of the books
def index(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        "user": user,
        "books": Book.objects.order_by('title'),
        "reviews": Review.objects.order_by('-created_at')[:3],
    }
    return render(request, 'book/index.html', context)

def add_book(request):
    context = {
        "authors": Author.objects.order_by('name')
    }
    return render(request, 'book/book_add.html', context)

def handle_add_book(request):
    title = request.POST['title']
    author_name = request.POST['author']
    review_text = request.POST['review']
    rating = request.POST['rating']
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)

    if len(Book.objects.filter(title=title)) == 1:
        #book already exists, add the review and redirect to book page
        old_book = Book.objects.get(title=title)
        new_review = Review.objects.create(text=review_text, rating=rating, user=user, book=old_book)
        url = reverse('show_book', kwargs={'book_id': old_book.id})
        return redirect(reverse('books'))
        
        #reverse url with book.id
        #httpresponseredirect to book page, and flash a message!
    else:
        #new/old author check
        if len(Author.objects.filter(name__icontains=author_name)) == 1:
            #author already exists if the length is 1. 
            author = Author.objects.get(name__icontains=author_name)
        else: #if length is 0
            author = Author.objects.create(name=author_name)

        new_book = Book.objects.create(title=title, author=author)
        new_review = Review.objects.create(text=review_text, rating=rating, user=user, book=new_book)
        url = reverse('show_book', kwargs={'book_id': new_book.id})
        return redirect(reverse('books'))

def show_book(request, book_id):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        "user": user,
        "books": Book.objects.get(id=book_id),
    }
    return render(request, 'book/book_show.html', context)


def handle_add_review(request, book_id):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    print book
    print user

    if request.method == 'POST':
        review_text = request.POST['review']
        rating = request.POST['rating']
        
        new_review = Review.objects.create(text=review_text, rating=rating, user=user, book=book)

        url = reverse('show_book', kwargs={'book_id': book.id})
        return HttpResponseRedirect(url)

def show_user(request, user_id):
     context = {
         "user": User.objects.annotate(number_of_reviews=Count('reviewers')).get(id=user_id),
         "reviews": Review.objects.filter(user__id=user_id),
     }
     return render(request, 'book/user_show.html', context)


# def delete_review(request, id):
#     if request.method == "POST":
#         review = Review.objects.get(id=id)
#         current_user = User.objects.currentUser(request)

#         if current_user.id == Review.user.id:
#             review.delete()

#     return redirect(reverse('success'))