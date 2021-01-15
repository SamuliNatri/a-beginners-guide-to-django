from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm, TodoDeleteForm


def index(request):
    todos = Todo.objects.all()
    
    paginator = Paginator(todos, 2)
    page = request.GET.get('page')
    todos = paginator.get_page(page)

    return render(request, 
        'todo/index.html',
        {'todos': todos}
    )


def detail(request, slug=None):
    todo = get_object_or_404(Todo, slug=slug)
    return render(request, 
        'todo/detail.html',
        {'todo': todo}
    )


@permission_required('todo.add_todo')
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TodoForm()
    return render(request, 'todo/add.html',
                  {'form': form})


@permission_required('todo.change_todo')
def edit(request, pk=None):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST,
                        instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html',
                  {'form': form,
		  'todo': todo})


@permission_required('todo.delete_todo')
def delete(request, pk=None):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoDeleteForm(request.POST,
                              instance=todo)
        if form.is_valid():
            todo.delete()
            return redirect('todo:index')
    else:
        form = TodoDeleteForm(instance=todo)
    return render(request,
                  'todo/delete.html',
                  {'form': form,
		  'todo': todo})
