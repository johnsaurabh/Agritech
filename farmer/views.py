from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Merchandiser,LatestPost,Schemes,Farmer
from django.core.mail import send_mail


def index(request):
    user = request.user 
    print(user)
    posts = LatestPost.objects.all()
    sch = Schemes.objects.all()
    context = {'user':user,'post':posts,'sch':sch}

    return render(request,'farmer/post.html',context)


def guide(request):
    return render(request,'farmer/guide.html')

def user_logout(request) :
    logout (request)
    return redirect(to=index)



def loan(request):
    if request.user.is_authenticated:
        return render(request,'farmer/loan.html')
    else :
        return redirect(to=login_view)



def schemes(request):
    sch = Schemes.objects.all()
    context = {'sch':sch,}
    return render(request,'farmer/schemes.html',context)
    
     

def retailers(request):
    if request.user.is_authenticated:
        mers = Merchandiser.objects.all()
        context={
        'retailer_details':mers,
        }
        return render(request,'farmer/retailers.html',context)
    else :
        return redirect(to=login_view)

def merch(request):
    farmer = Farmer.objects.all()
    context ={'farmer':farmer,}
    try:
        m = Merchandiser.objects.get(user=request.user)
        if m is not None:
            return render(request,'farmer/merch.html',context)
        else:
            return redirect(to=index)

    except:
        return redirect(to=index)



    

def login_view(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                farmer = Farmer.objects.get(user=user)
                if farmer is not None:
                    return redirect(to=index)
                else:
                    return redirect(to=merch)



            except:
                return redirect(to=merch)
 

            
    else:
        return render(request,'farmer/login.html',)
def applyLoan(request):
    send_mail(
    'Subject',
    'Message.',
    'balgurikalyan711@gmail.com',
    ['revantark@gmail.com'],
    )
    return HttpResponse("Success")

def sign_up(request):
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        brand = request.POST.get('brand')
        aid = request.POST.get('aid')
        user = User.objects.create_user(username, email=email, password=password)
        phone = request.POST.get('phone')
        merchandiser = Merchandiser(user=user,brand_name=brand,aadhar_ID=aid,phone=phone)
        merchandiser.save()
        user.save()
        return redirect(to=login_view)
    else:
        return render(request,'signup.html',)

