from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the first app")

def my_view(request):
    return render(request, 'index.html')
