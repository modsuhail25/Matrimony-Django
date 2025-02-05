from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from .forms import Detail
from django.contrib import messages
from django.contrib.auth import  logout

# Create your views here.
def index(request):
    return render(request, 'index.html')
def demoindex(request):
    return render(request, 'demoindex.html')
def admin(request):
    all=DetailRegister.objects.all()
    return render(request, 'admin.html',{'all':all})


def detail(request,id):
    d= get_object_or_404 (DetailRegister,id=id)
    if request.method=="POST":
        form=Detail(request.POST,instance=d)
        if form.is_valid():
            form.save()
            return redirect('/personal/')    
    else:
        form=Detail(instance=d)    
    return render(request, 'detail.html',{'form':form})

def about(request):
    return render(request, 'about.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

def blog(request):
    return render(request, 'blog.html')



def contact(request):
    return render(request, 'contact.html')



def event(request):
    return render(request, 'event.html')

def gallery(request):
    return render(request, 'gallery.html')
def personal(request):
    ids=request.session['session1']
    p=DetailRegister.objects.filter(id=ids).count()
    if p==0:
        return render(request,"login.html")
    else:
        p=DetailRegister.objects.filter(id=ids)

    return render(request, 'personal.html',{'p':p})

def message(request):
    messages.warning(request,"we will contact you soon ")
    return render(request,"message.html")
    
def list_detail(request,id):
    r=DetailRegister.objects.filter(id=id)
    return render(request, 'list_detail.html',{'r':r})

def list(request):
    r=DetailRegister.objects.all()
    return render(request, 'list.html',{'r':r})

def list1(request):
    b=DetailRegister.objects.all()

    return render(request, 'list1.html',{'b':b})

def bride(request):
    b=DetailRegister.objects.filter(partner="bride")

    return render(request, 'bride.html',{'b':b})
def groom(request):
    b=DetailRegister.objects.filter(partner="groom")

    return render(request, 'groom.html',{'b':b})



def search(request):
    if request.method=="POST":
        religion=request.POST['religion']

        s= DetailRegister.objects.filter(religion__contains=religion)
        context={'data1':religion,'s':s}
        return render(request,'search.html',context)
    else:
        return render(request, 'search.html',{})

def filter(request):

    return render(request,"filter.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        log=DetailRegister.objects.get(email=email,password=password)
        request.session['session1']=log.id
        return redirect('/personal/')

    return render(request, 'login.html')
def adminlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if email=="admin@gmail.com":
            if password=="main@123":
                return redirect("/admins/")
    return render(request,"adminlogin.html")
def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        height=request.POST['height']
        religion=request.POST['religion']
        caste=request.POST['caste']
        location=request.POST['location']
        education=request.POST['edu']
        profession=request.POST['profession']
        annual=request.POST['income']
        email=request.POST['email']
        password=request.POST['password']
        image=request.FILES['image']
        DetailRegister(name=name,age=age,height=height,religion=religion,caste=caste,location=location,education=education,profession=profession,annualincome=annual,email=email,password=password,image=image).save()  
        return redirect("/login/")   
    return render(request, 'register.html')



def team(request):
    return render(request, 'team.html')
def logout_user(request):
    logout(request)
    request.session.flush()  # Clears all session data

    return render(request,'demoindex.html')

def update(request,id):
    d=DetailRegister.objects.filter(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        height=request.POST['height']
        religion=request.POST['religion']
        caste=request.POST['caste']
        location=request.POST['location']
        education=request.POST['edu']
        profession=request.POST['profession']
        annual=request.POST['income']
        email=request.POST['email']
        image=request.FILES['image']
        DetailRegister.objects.filter(id=id).update(name=name,age=age,height=height,religion=religion,caste=caste,location=location,education=education,profession=profession,annualincome=annual,email=email,image=image) 
        return redirect("/personal/")
    return render(request, 'update.html',{'d':d})




def delete(request,id):
    DetailRegister.objects.filter(id=id).delete()
    return render(request,"personal.html")







