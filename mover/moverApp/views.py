from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required(login_url='loginPage')
def SignUpPage(request):
    if request.user.is_authenticated:
        return redirect('Dashboard')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account was created for" + user)
                return redirect("loginPage")
        context ={"form":form}
        return render(request, "signup.html", context)


# @login_required(login_url='loginPage')
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('Dashboard')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Dashboard')
            else:
                messages.info(request, "username or password is incorrect")
        context={}
        return render(request, 'login.html', context)


# @login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def DashBoard(request):
    context={}
    return render(request,"dashboard.html",context)

def Transaction(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        pass