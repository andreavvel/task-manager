from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_news(request):

    #Get data from DB
    news = News.objects.order_by('-create_time')
    # Create a dictionary containing the db entries
    # in a variable called news
    context = {'news': news}
    # Send the rendered site with
    # DB data
    # elements from the context dictionary
    # are used in news/index.html
    return render(request, 'news/index.html', context)

def get(request, id):
    #func get_object_or_404 returns an element from the database data with a given arg value
    #or sends an error to the client
    news= get_object_or_404(News, id=id)
    formatted_last_edit_time = news.last_edit_time.strftime("%B %d, %Y, %I:%M %p")  # Format the datetime
    context = {'news': news, 'formatted_last_edit_time': formatted_last_edit_time}  # Pass the formatted time to the context
    return render(request, 'news/show.html', context)
    
@login_required(login_url='/login/')
def add(request):
    #Checking the method of the HTTP request
    # If POST - we are looking for data in the body of the query
    # If GET - send the form to be filled in
    # (you can send data in the GET query -
    # but in this solution we do not use it)
    if request.method == 'POST':
        # Forms in Django allow you to validate data
        # so we create the form object from the query
        form = NewsForm(request.POST)
        # If the form - i.e. data sent from the POST query
        # are correct add an element to the database
        if form.is_valid():
            news = form.save(commit=False)
            # news.author = request.user
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect(view_news)
        # If they are not correct, we send the form back to the client
        # The automatic validator also creates error fields that are accessible from
        # the client side
        else:
            context = {'form': form}
            return render(request, 'news/add.html', context)
    # If a GET query is sent an empty form
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)

@login_required(login_url='/login/')  # Requires authentication
def edit_data(request, id):
    instance = get_object_or_404(News, id=id)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=instance)
        if form.is_valid():
            news= form.save(commit=False)
            news.last_edit_time = timezone.now()
            news.save()

            return redirect(view_news)  # Redirect to a relevant view after editing
    else:
        form = NewsForm(instance=instance)
    
    context = {'form': form, 'news': instance}
    return render(request, 'news/edit.html', context)    