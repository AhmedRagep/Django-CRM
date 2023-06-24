from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register
# Create your views here.

def home(request):
    # check login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You Have Logged In')
            return redirect('home')
        else:
            messages.success(request,'someone tried to log in and failed')
            return redirect('home')
    return render(request, 'home.html', {})



def user_logout(request):
    logout(request)
    messages.success(request, 'You Have Logged Out....')
    return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,'You Have Registerd Saccessfully! Welcome')
            return redirect('home')
    else:
        form = Register()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})