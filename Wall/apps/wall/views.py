from django.shortcuts import render
# import re
# import os, binascii
# import md5


# Create your views here.
def index(request):
	return render(request, 'wall/index.html')

def register(request):
    return render(request, 'wall/register.html')
    
# #Action for submitting registration form
# def handle_registration():
# 	if method == 'POST':
# 		passed = True
# 		query = "INSERT INTO users (first_name, last_name, username, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :username, :email, :hashed_pw, :salt, NOW(), NOW())"
# 		data = {}

# 		#first_name validation
# 		if len(request.POST['first_name']) > 1 and len(request.POST['first_name']) < 51:
# 			data["first_name"] = request.POST['first_name']
# 		else:
# 			flash("First name must be at least 2 characters!")
# 			passed = False

# 		#last_name validation
# 		if len(request.POST['last_name']) > 1 and len(request.POST['last_name']) < 51:
# 			data["last_name"] = request.POST['last_name']
# 		else:
# 			flash("Last name must be at least 2 characters!")
# 			passed = False

# 		#username validation
# 		if len(request.POST['username']) > 1:
# 			data["username"] = request.POST['username']
# 		else:
# 			flash("Must enter username!")
# 			passed = False

# 		#email validation
# 		if len(request.POST['email']) < 1:
# 			flash("Email cannot be blank!")
# 			passed = False
# 		elif not EMAIL_REGEX.match(request.POST['email']):
# 			flash("Invalid Email Address!")
# 			passed = False
# 		else:
# 			data["email"] = request.POST['email']

# 		#password validation
# 		if len(request.POST['password']) < 8:
# 			flash("Password must be at least 8 characters long.")
# 			passed = False
# 		elif request.POST['password'] != request.POST['confirm_password']:
# 			flash("Passwords do not match.")
# 			passed = False
# 		else:
# 			password = request.POST['password']
# 			salt = binascii.b2a_hex(os.urandom(15))
# 			hashed_pw = md5.new(password + salt).hexdigest()
# 			data['salt'] = salt
# 			data['hashed_pw'] = hashed_pw

# 		if passed:
# 			user_id = Model(query, data)
# 			flash("Successfully registered!")
# 			session['id'] = user_id
# 			return redirect('/success')
# 		else:
# 			return redirect('/register')

#Login page
def login(request):
    return render(request, 'wall/login.html')

# #Action for submitting login
# def handle_login():
# 	if method == 'POST':
# 		_username = request.form['username']
# 		password = request.form['password']
# 		user_query = "SELECT users.id, users.username, users.password, users.salt FROM users WHERE users.username = :user_name LIMIT 1"
# 		query_data = {'user_name': _username}


# 		user = mysql.query_db(user_query, query_data)
# 		print "Printing data from login", user
# 		if len(user) != 0:
# 		    test_password = md5.new(password + user[0]['salt']).hexdigest()
# 		    print user[0]['password']
# 		    print test_password
# 		    if user[0]['password'] == test_password:
# 		        flash("Successfully logged in!")
# 		        session['id'] = user[0]['id']
# 		        return redirect('/success')
# 		    else:
# 		        flash("Invalid login password. Please try again.")
# 		        return redirect('/login')
# 		else:
# 		    flash("Username not in database. Try again.")
# 		    return redirect('/login')

#Success Page
def success():
	#only displays if logged in 
	if not session['id']:
		return redirect('/login')
	else:
		return render(request, 'wall/success.html')

# #post message
# def handle_post():
# 	if method == 'POST':
# 	    passed = True
# 	    sid = session['id']
# 	    message_query = "INSERT INTO messages (user_id, content, created_at, updated_at) VALUES (:user_id, :content, NOW(), NOW())"
# 	    message_data = {'user_id': sid}
	    

# 	    #validate post
# 	    if len(request.POST['content']) > 1:
# 	        message_data["content"] = request.POST['content']
# 	    else:
# 	        flash("You must some type of content in your post")
# 	        passed = False

# 	    if passed:
# 	        sid = session['id']
# 	        mysql.query_db(message_query, message_data)
# 	        flash("Successfully submitted a post!")
# 	        return redirect('/success')
# 	    else:
# 	        flash("ohhhhhhh noooo")
# 	        return redirect('/')