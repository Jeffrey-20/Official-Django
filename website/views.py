from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib import messages
from .models import Gamedata

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout Success")
    return redirect('login')

def login(request):
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password = password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            
    context = {'form':form,
               'age': 2025}


    return render(request, 'pages/login.html', context = context)


#create a form
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            
            return redirect('login')
    
    context = {'form': form}
            

    return render(request, 'pages/register.html', context=context)

@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'pages/dashboard.html', context=context)
 

@login_required(login_url="login")
def create_record(request):

    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Your record was created")
            return redirect("dashboard")
    
    context = {"create_form": form}
    return render(request, 'pages/create-record.html',context=context)

@login_required(login_url="login")
def singular_record(request, pk):
    one_record = Record.objects.get(id=pk)
    context = {'record': one_record}
    return render(request, 'pages/view-record.html',context=context)


@login_required(login_url="login")
def update_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    update_form = CreateRecordForm(instance=record)

    if request.method == "POST":
        update_form = CreateRecordForm(request.POST, instance=record)
        if update_form.is_valid():
            update_form.save()
            return redirect('dashboard')

    return render(request,"pages/update_record.html",{"update_form":update_form})


@login_required(login_url="login")
def view_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    return render(request, "pages/view_record.html", {"record":record})

@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Your record was deleted")
    return redirect("dashboard")

@login_required(login_url="login")
def games(request):
    return render(request,'pages/games.html')

@login_required(login_url="login")
def game_date(request):
    data = Gamedata.objects.all()
    context = {'data': data}

    return render(request, 'pages/game-data.html', context = context)