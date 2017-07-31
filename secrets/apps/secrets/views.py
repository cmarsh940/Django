from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from ..login_register.models import User
from .models import Secret

def index(request):
    current_user = User.objects.currentUser(request)
    secrets = Secret.objects.annotate(num_likes=Count('liked_by'))

    # if i need to put likes in order by most likes also ([:3] says to just get the top 3 likes)
    # secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')[:3]

# context = the user and the secret when the index page is loaded.
    context = {
        'user': current_user,
        'secrets': secrets,
    }

    return render(request, 'secrets/index.html', context)


# create the content post controller

def create(request):
    if request.method == "POST":

        if len(request.POST['content']) != 0:
            current_user = User.objects.currentUser(request)

            secret = Secret.objects.createSecret(request.POST, current_user)

    return redirect(reverse('success'))


# create the like controller

def like(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.add(secret)

    return redirect(reverse('success'))



# Create the unlike controller

def unlike(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.remove(secret)

    return redirect(reverse('success'))


# Create the delete controller

def delete(request, id):
    if request.method == "POST":
        secret = Secret.objects.get(id=id)
        current_user = User.objects.currentUser(request)

        if current_user.id == secret.user.id:
            secret.delete()

    return redirect(reverse('success'))



