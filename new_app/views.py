from django.shortcuts import render

# Create your views here.
def site(request):
    return render(request,'view.html')
def home(request):
    return render(request,'index.html')
def dashbord(request):
    return render(request,'index2.html')