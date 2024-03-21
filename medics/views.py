from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 
from django.contrib.auth import logout

@login_required(login_url='/login/')
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =CustomerForm()
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')
def product_read(request):
    med_list=Customer.objects.all()
    return render(request,'retrieve.html',{'med_list':med_list})


@login_required(login_url='/login/')
def product_update(request, pk):
    med = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=med)
        if form.is_valid():
            form.save()
            return redirect('listmed')
    else:
        form =CustomerForm(instance=med)           
    return render(request, 'update.html', {'form': form})


@login_required(login_url='/login/')
def product_delete(request,pk):
    med=Customer.objects.get(pk=pk)  
    if request.method == 'POST':
        med.delete()
        return redirect('listmed')
    
    return render(request,'delete.html',{'med':med})

@login_required(login_url='/login/')
def search_item(request):
    search_term = request.GET.get('search', '')
    items = Customer.objects.filter(Name__istartswith=search_term).values()
    message="no object found"
    if not search_term:
        return render(request,'home.html',{'message':message})
    if items:
        return render(request,'home.html',{'items':items})   
    else :
        return render(request, 'home.html', {'message': message})



