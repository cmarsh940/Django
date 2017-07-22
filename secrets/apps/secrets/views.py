from django.shortcuts import render, redirect
from .models import User
 
# Create your views here.
def index(request):
	return render(request, 'secrets/index.html')

def success(request):
	if 'user_id' in request.session:

		return render(request, 'secrets/success.html')

	return redirect('/')

def register(request):
	if request.method == 'POST':
		errors = User.objects.validRegistration(request.POST)

		if not errors:
			user = User.objects.createUser(request.POST)

			request.session['user_id'] = user.id

			return redirect('/success')

		print errors

	return redirect('/')

def login(request):
	if request.method == 'POST':
		errors = User.objects.validLogin(request.POST)

		if not errors:
			user = User.objects.createUser(request.POST)

		if user:
			password = str(request.POST['password'])
			user_password = str(user.password)

			hashed_pw = bcrypt.hashpw(password, user_password)

			if hashed_pw == user.password:
				request.session['user_id'] = user.id

					return redirect('/success')

			errors.append("invalid account information.")

		print errors
		
	return redirect('/')


	return redirect('/')

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')

	return redirect('/')
	pass