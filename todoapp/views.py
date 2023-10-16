from django.shortcuts import render, redirect

from todoapp.forms import todoForm
from todoapp.models import todo


# Create your views here.

def base(request):
    return render(request,'base.html')


def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

# create  the  todolist to db

def create(request):
    form = todoForm()
    print(form)
    if request.method == 'POST':
        data = todoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/')
    return render(request,'index2.html',{'form':form})

# read the todolist
def read(request):
    data = todo.objects.all()
    print(data)
    return render(request,'index4.html',{'data':data})

def delete(request,id):
    if request.method == 'POST':
        data = todo.objects.get(id=id)
        print(data)
        data.delete()
        return redirect('read')
    
