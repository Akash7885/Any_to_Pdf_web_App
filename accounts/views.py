from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name)
                user.save()
                messages.info(request,"User Successfully Created")

        else:
            messages.info(request, 'Password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request,user.username +" Successfully Login")
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
