from django.shortcuts import render, redirect
from .models import Student, Spec
# Create your views here.

def home(request):
    return render(request, 'alarm/home.html')

def new(request):
    return render(request,'alarm/newspec.html')

def create(request):
    spec=Spec()
    spec.tof = request.GET['tof']
    spec.gpa = request.GET['gpa']
    spec.when = request.GET['when']
    spec.country = request.GET['country']
    spec.univ_name = request.GET['univ_name']
    spec.kor_name = request.GET['kor_name']
    spec.depart = request.GET['depart']
    spec.save()
    return redirect('specboard')

def specboard(request):
    specs = Spec.objects
    return render(request,'alarm/specboard.html', {'specs':specs})

