from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.site,name="site"),
    path('index',views.home,name="site"),
    path('dashbord',views.dashbord,name="site"),
    path('forms',views.formConstruct,name='forms')
]