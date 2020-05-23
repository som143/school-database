from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.db.models import *

# Create your views here.
def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username= username,password=password1,email=email,first_name= first_name,last_name= last_name)
        user.save();
        print("user created")
        return redirect("/signin")
        # return redirect("/")
    else:
        return render(request,'registration.html')
def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username= username,password = password)
        if user is not None:

            auth.login(request,user)
            print("login created")
            return render(request,'registration.html', {"uname": username})
        else:
            print("invalid credentil")
            
    return render (request,'signin.html')



def home(request):
    strength = school.objects.all()
    for i in strength:
        print(i.strength)
    
    return render(request,'home.html',{'strength':strength})



def classes(request,classes=None):
    # school = details.objects.filter(classes= classes)
    school = details.objects.filter(classes= classes)
   
   
    for i in  school:
        print(i)
    return render(request,'class.html',{'classes':school})


def delete(request,id = None):
    school = details.objects.get(id = id)
    school.delete()
    return redirect('/classes')





def summary(request,day = None):
    school = details.objects.values('day','teacher_name').annotate(classes =  Count("classes")).order_by('-classes')
    for i in school:
        print(i)


    return render(request,'summery.html',{'school': school})


"""each add function adding each class """
def add(request):
    if request.method =='POST':
        if request.POST.get('day')or request.POST.get('present_strngth') or request.POST.get('sub')or request.POST.get('teacher_name'):
            cls_details = details()
            cls_details.day = request.POST.get('day')
            cls_details.present_strngth = request.POST.get('present_strngth')
            cls_details.sub= request.POST.get('sub')
            cls_details.teacher_name= request.POST.get('teacher_name')
            cls_details.id = request.POST.get("id") 
            cls_details.classes =  request.POST.get('classes')
            
            cls_details.save()
            print(cls_details.id)
            print("data saved")
            return redirect("/classes")
            # return render(request,'class.html',{"form":[cls_details]})
        else:
            return HttpResponse("some error occured")
    return render(request,'add_data/add.html')
def home_add(request):
    if request.method =='POST':
        if request.POST.get('classes')or request.POST.get('strength') or request.POST.get('cls_teacher'):
            sch_details = school()
            sch_details.classes = request.POST.get('classes')
            sch_details.strength = request.POST.get('strength')
            sch_details.cls_teacher= request.POST.get('cls_teacher')            
            sch_details.save()
            return redirect("/home")
            # return render(request,'class.html',{"form":[cls_details]})
        else:
            return HttpResponse("some error occured")
    return render(request,'add_data/home_add.html')


"""end each add function adding each class """