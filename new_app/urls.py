from django.urls import path

from new_app import views

urlpatterns = [
    path('test',views.site,name="site"),
    path('home',views.home,name="home"),
    path('dashbord',views.dashbord,name="dashbord"),
    path('forms',views.formConstruct,name='forms'),
    path('data',views.construct_view, name='data'),
    path('del/<int:id>/',views.construct_delete,name='del'),
    path('upd/<int:id>/',views.construct_update,name='upd')

]