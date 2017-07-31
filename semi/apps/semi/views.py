from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'semi/index.html')

def register(request):
    if request.method == 'POST':
        userObject = User.objects.isValidRegistration(request.POST)
        if 'user' in userObject:
            request.session['id'] = userObject['user'].id 
            request.session['first_name'] = userObject['user'].first_name 
            return redirect(reverse('product'))
        else:
            for error in userObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('index'))
    else:
        return redirect('index')

def login(request):
    if request.method == 'POST':
        userObject = User.objects.isValidLogin(request.POST)
        if 'user' in userObject:
            request.session['id'] = userObject['user'].id 
            request.session['first_name'] = userObject['user'].first_name
            return redirect(reverse('product'))
        else:
            for error in userObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('index'))


def logout(request):
    if 'user' in request.session:
        request.session.pop('user')

    return redirect(reverse('index'))





 # ######################################       #################################  #



def product(request):
	return render(request, 'semi/products.html')

def add_product(request):
    return render(request, 'semi/new.html')

def handle_add_product(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']

    if request.method == 'POST':

        product = Product.objects.create(name=name, description=description, price=price)

        return redirect(reverse('product'))