from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.index1,name='index1'),
    path('index2',views.index2,name='index2'),
    path('create',views.create,name='create'),
    path('base',views.base,name='base'),
    path('read',views.read,name='read'),
    path('delete/<int:id>/',views.delete,name='delete')

]