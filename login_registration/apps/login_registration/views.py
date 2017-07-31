from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register_page(request):
    return render(request, 'login_registration/registration.html')

def login_page(request):
    return render(request, 'login_registration/login.html')

def register(request):
    userObject = User.objects.isValidRegistration(request.POST)
    if 'user' in userObject:
        request.session['id'] = userObject['user'].id
        request.session['first_name'] = userObject['user'].first_name
        return redirect('success')
    else:
        for error in userObject['errors']:
            messages.warning(request, error)
        return redirect('register_page')

def login(request):
    if request.method == 'POST':
        userObject = User.objects.isValidLogin(request.POST)
        if 'user' in userObject:
            request.session['id'] = userObject['user'].id
            request.session['first_name'] = userObject['user'].first_name
            return redirect('success')
        else:
            for error in userObject['errors']:
                messages.warning(request, error)
            return redirect('login_page')

    return redirect('login_page')


def success(request):
    if 'id' in request.session:

        return render(request, 'login_registration/success.html')

    return redirect('/')

def logout(request):
    if request.method == 'POST':
        print "hi"

        if 'id' in request.session:
            print "hi2"
            request.session.set_expiry(0) 
            try:
                del request.session['id']
            except KeyError:
                pass
            request.session.modified = True
            return redirect('login_page')
    return redirect('success')