from django.shortcuts import render

from new_app.forms import Constructionform
from new_app.models import Construction


# Create your views here.
def site(request):
    return render(request,'view.html')
def home(request):
    return render(request,'index.html')
def dashbord(request):
    return render(request,'index2.html')




def formConstruct(request):
    form = Constructionform()

    if request.method == 'POST':
        data = Constructionform(request.POST)
        if data.is_valid():

            data.save()
    return render(request,'form.html',{'form':form})

def construct_view(request):
    data = Construction.objects.all()
    return render(request, 'view_data.html',{'data':data})