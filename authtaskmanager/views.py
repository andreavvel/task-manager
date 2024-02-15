from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .utils import is_admin, is_regular_user

def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = form.cleaned_data['is_admin']
            user.save()
            login(request, user)
            return redirect('/taskmanager')  # Redirect to the desired page after signup
    else:
        form = CustomUserCreationForm()

    return render(request, 'authtaskmanager/signup.html', {'form': form})

def log_in(request):
    # Checking if the user is logged in
    # If so - redirect them to the page with the message list
    if request.user.is_authenticated:
        return redirect('/taskmanager')
        
    # Checking the type of HTTP request
    # If POST user login attempt
    if request.method == 'POST':
        # Using the form to check if all data have been entered
        form = LoginForm(request.POST)
        if form.is_valid():
            # Using Django's built-in authentication system
            # to check if the user exists in the database
            user = authenticate(
            request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
            )
            # If the user exists - log them in
            # and redirect to news page
            if user is not None:
                login(request, user)
                return redirect('/taskmanager')
            # If they do not exist or the data sent is incomplete - send it
            # back to the customer with the data form
            else:
                context = {'form': form}
                return render(request, 'authtaskmanager/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authtaskmanager/login.html', context)
    # If GET - send an empty form
    else:
        context = {'form': LoginForm()}
        return render(request, 'authtaskmanager/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/taskmanager')

@user_passes_test(is_admin)
def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'authtaskmanager/userlist.html', {'users': users})
