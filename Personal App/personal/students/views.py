from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
from .miscellaneous import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime

# Create your views here.
def see_all(request):
    stu_class=studs.objects.all()
    context={
        'stu_class':stu_class,
    }
    return render(request,"students/all databases.html",context)

def student(request,roll):
    student_info=studs.objects.get(roll=roll)
    context={
        'student':student_info,
    }
    return render(request,"students/student.html",context)

def search(request):
    form = roll_s()
    if request.method == 'POST':
        form = roll_s(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/students/{request.POST['roll']}")
    context={
        'form':form,
        }
    return render(request, 'students/get_info.html', context)

def index(request):
    if request.method=="POST":
        form =indexes(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"{request.POST['choice']}/")
    else:
        form=indexes()
    context={
        'form':form,
    }
    return render(request,"students/index.html",context)

def ent_info(request):
    form=ent_infos()
    if request.method == 'POST':
        form = ent_infos(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/students/{request.POST['roll']}/")

    context={
        'form':form,
    }
    return render(request,"students/ent_info.html",context)

def completed(request):
    context={}
    return render(request,"students/completed.html",context)

# Have to create update one (when visiting update, This is called first)
def update(request):
    form = roll_s()
    if request.method == 'POST':
        if object_exists({"roll":request.POST['roll']},model="studs")==False:
            messages.error(request,f"The roll Number {request.POST['roll']} does not exist")
            return HttpResponseRedirect("/students/update/")
        form = roll_s(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/students/update/{request.POST['roll']}")
    context={
        'form':form,
        }
    return render(request, 'students/get_info.html',context)


def update_roll(request,roll_no):
    student_info=studs.objects.get(roll=roll_no)
    form=ent_infos(instance=student_info)
    if request.method=="POST":
        form=ent_infos(request.POST,instance=student_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/students/{roll_no}/")
    context={
        "form":form,
        }
    return render(request,"students/update_info.html",context)

def registration(request):
    form=user_create()
    if request.method=="POST":
        form=user_create(request.POST)
        if duplicate_entries_preventer(factor={'email':request.POST["email"]},model="User"):
            messages.error(request,"Email Already Exists, Please use a different email")
            return HttpResponseRedirect("/students/registration/")
        if form.is_valid():
            form.save()
            messages.success(request,"Signed-Up Succesfully")
            add_to_students(User.objects.get(username=request.POST["username"]))
            studs.objects.create(name=request.POST["first_name"]+" "+request.POST["last_name"],email=request.POST["email"])
            return HttpResponseRedirect("/students/login/")

    context={
        "form":form,
        }
    return render(request,"students/registration.html",context)
def logins(request):
    form=user_sign()
    if request.method=="POST":
        users=authenticate(username=request.POST["username"],password=request.POST["password"])
        if users != None:
            login(request,users)
            messages.success(request,f"Welcome {request.user.first_name}, You have Logged In Succesfully")
            return HttpResponseRedirect("/students/completed")
        else:
            messages.error(request,"Email/Password does not exist")
            return HttpResponseRedirect("/students/login/")
    context={
        "form":form,
        }
    return render(request,"students/login.html",context)
def logouts(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfull")
        return HttpResponseRedirect("/students/login/")
    else:
        messages.error(request,"Logout failed, Not Logged in currently")
        return HttpResponseRedirect("/students/login/")

def take_attendance(request):
    users=[x for x in studs.objects.all()]
    if request.method=="POST":
        users=[x.roll for x in studs.objects.all()]
        # print(request.POST)
        attended_students=[x for x in request.POST if request.POST[x]=="on"]
        for x in users:
            if str(x) in attended_students:
                object_creator(factor={'roll_id':x,'date':format(datetime.now(),"%Y-%m-%d"),'attend':1},model="attendance")
            else:
                object_creator(factor={'roll_id':x,'date':format(datetime.now(),"%Y-%m-%d"),'attend':0},model="attendance")
        return HttpResponseRedirect("/students/take_attendance/") 
    context={
        "users":users,
        }
    return render(request,"students/staff_attendance.html",context)