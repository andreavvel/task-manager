from django.urls import path
from . import views
from .views import add, get, edit_data

urlpatterns = [
    path('', views.view_news, name='news_section'),
    path('add/', add, name="add"),
    path('<int:id>/',get, name='get'),
    path('edit/<int:id>/', edit_data, name='edit_data'),
    # Add more URL patterns here as needed
]
