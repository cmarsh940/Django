from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'username_validation/index.html', context)

def handle_registration(request):
	if not User.objects.doesUsernameExist(request.POST['username']):
		if User.objects.isValidUsername(request.POST['username']):
			User.objects.create(username=request.POST['username'])
			messages.success(request, 'The user ' + request.POST['username']+ ' is valid')
			return redirect('success')
		else:
			messages.warning(request, 'Invalid username please enter a email as a username')
			return redirect('index')
	else:
		print "Username already exists"
		messages.warning(request, 'Username Already Exists')
		return redirect('index')

def success(request):
	context = {
		"users": User.objects.all()
	}
	return render(request, 'username_validation/success.html', context)

def destroy(request, user_id):
	User.objects.filter(id=int(user_id)).delete()
	return redirect('success')