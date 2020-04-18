from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    if request.method == 'GET':
        result = Products.objects.all()
        return render(request, 'home.html', {'home':result})

def InsertProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ProductForm()
    
    return render(request, 'product_upload.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded!')

def ShowProducts(request):
    if request.method == 'GET':
        result = Products.objects.all()
        return render(request, 'show_products.html', {'productlist':result})

def product_detail(request, product_id):
    detail = Products.objects.filter(id=product_id)
    return render(request, 'product.html',{'product_detail':detail})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productlist')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error = True
            return render(request, 'login.html', {'error': error}) 

    return render(request, 'login.html',)

def userLogout(request):
    logout(request)
    return redirect('home')

def add_to_cart(request, product_id):
    if request.user.is_authenticated():
        try:
            product = Products.objects.get(pk=product_id)
        except ObjectDoesNotExist:
