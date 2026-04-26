from django.shortcuts import render
from django.shortcuts import  redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def sign_up_view(request):
    
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            new_user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            new_user.save()
            print(f"new user -> {new_user.username} has signed up")
            #ts myby needs the views.name one but idk
            return redirect('accounts:log_in')
        
        except Exception as e:
            print(e)
    return render(request, 'accounts/signup.html', {})

def sign_in_view(request):
    if request.method == "POST":

        #checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            #login the user
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")


    return render(request, 'accounts/login.html', {})

def log_out(request):
    logout(request)
    messages.success(request, "logged out successfully", "alert-warning")

    return redirect(request.GET.get("next", "/"))

