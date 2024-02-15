from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import log_in, log_out, signUp, user_list

urlpatterns = [
    path('login/', log_in),
    path('logout/', log_out),
    path('signup/', signUp),
    path('userlist/', user_list),
]
