from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register,AddForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records':records})



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


def customer_record(request,pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        return render(request, 'record.html', {'record':record})
    else:
        messages.success(request,'You Have Logged In To View This Page')
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
      delete = get_object_or_404(Record, id=pk)
      delete.delete()
      messages.success(request,'Record Deleted successfully...')
      return redirect('home')    
    else:
        messages.success(request,'You Have Logged In To View This Page')
        return redirect('home')
    

def add_record(request):
    form = AddForm(request.POST, None)
    if request.user.is_authenticated:
      if request.method == 'POST':
          if form.is_valid():
            add_record = form.save()
            messages.success(request,'Record Added')
            return redirect('home')
      return render(request, 'add.html', {'form':form})
    else:
        messages.success(request,'You Have Logged In To View This Page')
        return redirect('home')
        
    
def update_record(request, pk):
    if request.user.is_authenticated:
      update = get_object_or_404(Record,id=pk)
      form = AddForm(request.POST or None, instance=update)
      if request.method=='POST':
          if form.is_valid():
            form.save()
            messages.success(request,'You Have Update Record!')
            return redirect('home')
      return render(request, 'update.html', {'form':form,'update':update})
    else:
        messages.success(request,'You Have Logged In To View This Page')
        return redirect('home')