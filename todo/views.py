from django.shortcuts import render,redirect,get_object_or_404
from todo.forms import TodoForm,ContactForm #importing forms from forms.py
from todo.models import Todo #configuring models.py and views.py

# Create your views here.

def home(request):
    return render(request,'home.html')
#inserting the values from forms.py to database

def todoadd(request):
    todoform=TodoForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")
    return render(request,'todoadd.html',{'forms':todoform})


def todolist(request):
    allfeedback=Todo.objects.all()
    return render(request,'todolist.html',{'all':allfeedback})

def contact(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect("home")
    return render(request,'contact.html',{'forms':contactform})

def about(request):
    return render(request,'about.html')

def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    todoform=TodoForm (request.POST or None, instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")
    return render (request,'todoadd.html', {'forms': todoform})

def tododelete(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        todo.delete()
        return redirect("todolist") 
    return render(request,'tododelete.html',{'todo':todo})     