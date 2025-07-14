from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,"home.html",{})

def contact(request):
    if request.method=="POST":
        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']

        #send e-mail
        # send_mail(

        # name #who send it 
        # email #his email 
        # phone # thlephono
        # subject #thema 
        # message #to mhnyma
        # ['...'] # natalia
        # )


        return render(request,"contact.html",{'name':name})
    else:
        return render(request,"contact.html",{})


def about(request):
    return render(request,"about.html",{})

def index(request):
    return render(request,"index.html",{})

def projects(request):
    return render(request,"projects.html",{})

def services(request):
    return render(request,"services.html",{})


    
def studio(request):
    return render(request,"studio.html",{})


def commercial(request):
    return render(request,"commercial.html",{})