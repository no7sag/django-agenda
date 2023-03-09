from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
from django.contrib import messages

def index(request):
    todos = ToDo.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'todos': todos,
    }

    return render(request, 'todo/index.html', context)

def view(request, id):
    todo = ToDo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todo = ToDo.objects.get(id=id)

    if request.method == 'GET':
        form = ToDoForm(instance = todo)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'todo/edit.html', context)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id,
        }
        messages.success(request, 'To do updated.')
        return render(request, 'todo/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = ToDoForm()
        context = {
            'form': form,
        }
        return render(request, 'todo/create.html', context)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('todo')

def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('todo')