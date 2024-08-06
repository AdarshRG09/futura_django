from django.shortcuts import render

from new_app.forms import Construction, Constructionform


# Create your views here.
def site(request):
    return render(request,'view.html')
def home(request):
    return render(request,'index.html')
def dashbord(request):
    return render(request,'index2.html')




def formConstruct(request):
    form = Constructionform()
    return render(request,'form.html',{'form':form})