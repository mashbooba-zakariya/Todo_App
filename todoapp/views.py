from django.shortcuts import render, redirect

from todoapp.forms import todoForm


# Create your views here.
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
            return redirect('/')
    return render(request,'index2.html',{'form':form})
