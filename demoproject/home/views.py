from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


# Create your views here.

# def home1(request):
#     return render(request,'home1.html')

def home2(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'home2.html', {'products': products})


def registration(request):
    if request.method == 'POST':
        username = request.POST['txt_username']  #[TEXTNAME NAME]
        password = request.POST['txt_password1']
        con_password = request.POST['txt_password2']
        fname = request.POST['txt_fname']
        lname = request.POST['txt_lname']
        email = request.POST['txt_email']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('login')
    return render(request, 'registration.html')


# def logout(request):
#     return render(request, 'Signup.html')


def login(request):
    if request.method == "POST":
        userid = request.POST['txt_username']
        pass1 = request.POST['txt_password1']
        user = authenticate(username=userid, password=pass1)
        if user is not None:
            auth_login(request, user)
            f_name = user.first_name
            l_name = user.last_name
            return render(request, 'user_dashboard.html', {'fname': f_name, 'lname': l_name})
        else:
            messages.error(request, "Invalid Credentials")

            return redirect('login')

    return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('home2')


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Successfully added new Product")
            return redirect('home2')
    product_form = ProductForm()
    return render(request, 'add_product.html', {'form': product_form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES,instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect(home2)

    else:
        product_form=ProductForm(instance=product)
        return render(request,'edit_product.html',{'form':product_form})

def delete_product(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('home2')
    return render(request,'delete_product.html',{'product':product})


@login_required(login_url='login')
def user_dashboard(request):
    fname=request.user.first_name
    lname=request.user.lastname
    return render(request,'user_dashboard.html',{fname:fname,lname:lname})







