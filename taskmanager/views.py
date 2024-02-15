from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Task
from .forms import TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

@login_required(login_url='/login/')
def display_items(request):
    user_tasks = Task.objects.filter(user=request.user).order_by('due_date')
    paginator = Paginator(user_tasks, 10)  # Show 10 tasks per page

    page_number = request.GET.get('page')
    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    today_date = date.today()
    return render(request, 'taskmanager/display_items.html', {'items': items, 'today_date': today_date})

@login_required(login_url='/login/')
def add_item(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            # Additional processing or setting user-related data
            item.save()
            return redirect('taskmanager:display_items')  # Redirect to the display view
    else:
        form = TaskForm()
    return render(request, 'taskmanager/add_item.html', {'form': form})

@login_required(login_url='/login/')
def edit_item(request, item_id):
    item = get_object_or_404(Task, pk=item_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('taskmanager:display_items')  # Redirect after editing
    else:
        form = TaskForm(instance=item)
    return render(request, 'taskmanager/edit_item.html', {'form': form, 'item': item})

@login_required(login_url='/login/')
def delete_item(request, item_id):
    item = get_object_or_404(Task, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('taskmanager:display_items')  # Redirect after deletion
    return render(request, 'taskmanager/delete_item.html', {'item': item})
