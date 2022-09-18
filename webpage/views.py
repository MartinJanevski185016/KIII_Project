from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Youtube

class CreateUserForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
       'class':'form-control form-control-lg'
        })
        self.fields["email"].widget.attrs.update({
        'class':'form-control form-control-lg'
        })
        self.fields["password1"].widget.attrs.update({
        'class':'form-control form-control-lg'
        })
        self.fields["password2"].widget.attrs.update({
        'class':'form-control form-control-lg'
        })
     class Meta:
        model = User
        fields = ['username','email','password1','password2']

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def register(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')

    context={'form':form}
    return render(request,"register.html",context)
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password isn\'t matching')

    context={}
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def artstyle(request):
    videos = Youtube.objects.filter(id=1)
    context = {'videos': videos}
    return render(request, 'artstyle.html',context)
def bestsculpt(request):
    videos = Youtube.objects.filter(id=2)
    context = {'videos': videos}
    return render(request, 'bestsculpt.html',context)
def blendersculpting(request):
    videos = Youtube.objects.filter(id=3)
    context = {'videos': videos}
    return render(request, 'blendersculpting.html',context)
def buyatablet(request):
    videos = Youtube.objects.filter(id=4)
    context = {'videos': videos}
    return render(request, 'buyatablet.html',context)
def contact(request):
    return render(request, 'contact.html',{})
def courses(request):
    return render(request, 'courses.html',{})
def digitalpainting(request):
    videos = Youtube.objects.filter(id=5)
    context = {'videos': videos}
    return render(request, 'digitalpainting.html',context)
def glowinthedark(request):
    videos = Youtube.objects.filter(id=6)
    context = {'videos': videos}
    return render(request, 'glowinthedark.html',context)
def introphotoshop(request):
    videos = Youtube.objects.filter(id=7)
    context = {'videos': videos}
    return render(request, 'introphotoshop.html',context)
def photobashing(request):
    videos = Youtube.objects.filter(id=8)
    context = {'videos': videos}
    return render(request, 'photobashing.html',context)
def rig3dsmax(request):
    videos = Youtube.objects.filter(id=9)
    context = {'videos': videos}
    return render(request, 'rig3dsmax.html',context)
def rigblender(request):
    videos = Youtube.objects.filter(id=10)
    context = {'videos': videos}
    return render(request, 'rigblender.html',context)
def squashandstretch(request):
    videos = Youtube.objects.filter(id=11)
    context = {'videos': videos}
    return render(request, 'squash&stretch.html',context)
def walk_cycles(request):
    videos = Youtube.objects.filter(id=12)
    context = {'videos': videos}
    return render(request, 'walk_cycles.html',context)
def whytmanga(request):
    videos = Youtube.objects.filter(id=13)
    context = {'videos': videos}
    return render(request, 'whytmanga.html',context)
def imagebetter(request):
    videos = Youtube.objects.filter(id=14)
    context = {'videos': videos}
    return render(request, 'imagebetter.html',context)


