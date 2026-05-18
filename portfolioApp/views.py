from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def registerPage(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Registration successful.")
            return redirect('login')
        
    form = UserRegisterForm()
    context = {
        'form':form,
        'title':'Register Form',
        'btn':'Register'
    }
    return render(req,'base/baseAuthForm.html',context)

def loginPage(req):
    if req.method == 'POST':
        form = UserLoginForm(req,req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req,"Login successful.")
            return redirect('dashboard')
        
    form = UserLoginForm()
    context = {
        'form':form,
        'title':'Login Form',
        'btn':'Login'
    }
    return render(req,'base/baseAuthForm.html',context)

def personalInfoPage(req):
    if req.method == "POST":
        form = PersonalInfoForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,"PersonalInfo Page  Create successful.")
            return redirect('dashboard')
        
    form = PersonalInfoForm()
    context = {
        'form':form,
        'title':'Personal Info Form',
        'btn':'Create'
    }
    return render(req,'base/baseForm.html',context)

def workExperiencePage(req):
    if req.method == "POST":
        form = WorkExperienceForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
          
            messages.success(req,"Work Experience Page  Create successful.")
            return redirect('dashboard')
        
    form = WorkExperienceForm()
    context = {
        'form':form,
        'title':'Work Experience Form',
        'btn':'Create'
    }
    return render(req,'base/baseForm.html',context)

def educationPage(req):
    if req.method == "POST":
        form = EducationForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(req,"Education Page  Create successful.")
            return redirect('dashboard')
        
    form = EducationForm()
    context = {
        'form':form,
        'title':'Education Form',
        'btn':'Create'
    }
    return render(req,'base/baseForm.html',context)


def projectPage(req):
    if req.method == "POST":
        form = ProjectForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
           
            messages.success(req,"Project Page  Create successful.")
            return redirect('dashboard')
        
    form = ProjectForm()
    context = {
        'form':form,
        'title':'Project Form',
        'btn':'Create'
    }
    return render(req,'base/baseForm.html',context)

def technicalPage(req):
    if req.method == "POST":
        form = TechnicalForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(req,"Technical Page  Create successful.")
            return redirect('dashboard')
        
    form = TechnicalForm()
    context = {
        'form':form,
        'title':'Technical Form',
        'btn':'Create'
    }
    return render(req,'base/baseForm.html',context)


def dashboardPage(req):
    info = PersonalInfoModel.objects.all()
    work = WorkExperienceModel.objects.all()
    edu = EducationModel.objects.all()
    project = ProjectModel.objects.all()
    technical = TechnicalModel.objects.all()

    context = {
        'info':info,
        'work':work,
        'edu':edu,
        'project':project,
        'technical':technical,
    }
    return render(req,'page/dashboard.html',context)
