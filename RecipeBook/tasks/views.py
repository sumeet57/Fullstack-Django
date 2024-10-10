from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(author=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging line to print the POST data
        title = request.POST.get('title')
        author = request.user  # Assuming the author is the logged-in user

        # Check if all required fields are present
        if not title:
            return render(request, 'task_create.html', {'error': 'All fields are required.'})

        try:
            task = Task(title=title, author=author)
            task.save()
            return redirect('task_list')
        except TypeError as e:
            return render(request, 'task_create.html', {'error': str(e)})

    return render(request, 'task_create.html')

@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.user != task.author:
        return redirect('task_list')  # Ensure only the author can update the task

    if request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            return render(request, 'task_update.html', {'error': 'All fields are required.', 'task': task})
        
        try:
            task.title = title
            task.save()
            return redirect('task_list')
        except TypeError as e:
            return render(request, 'task_update.html', {'error': str(e), 'task': task})
    
    return render(request, 'task_update.html', {'task': task})

@login_required
def task_delete(request, pk):
    if request.user == Task.objects.get(pk=pk).author:
        Task.objects.get(pk=pk).delete()
        return redirect('task_list')
        
