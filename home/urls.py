from django.contrib import admin
from django.urls import path, include
from .views import my_view, index
from . import views
urlpatterns = [
#path('admin/', admin.site.urls),
path('', index, name='index'),  # Match the root URL for rendering "This is the first app"
path('template/', my_view, name='my_view'),
]


