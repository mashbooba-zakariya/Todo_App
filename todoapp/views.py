from django.contrib import messages
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
    if request.method == 'POST':
        data = todoForm(request.POST)
        if data.is_valid():
            data.save()
            messages.info(request, ' added succesfully')
            return redirect('read')
        else:
            messages.info(request, ' This date is past!!!')
    return render(request,'index2.html',{'form':form})

# read the todolist
def read(request):
    data = todo.objects.all()
    return render(request,'index4.html',{'data':data})

def delete(request,pk):
    if request.method == 'POST':
        data_id = todo.objects.get(id=pk)
        data_id.delete()
        return redirect('read')
    
def update(request,id):
    data = todo.objects.get(id=id)
    form = todoForm(instance=data)
    if request.method == 'POST':
        form = todoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request,'update.html',{'form':form})