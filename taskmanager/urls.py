from django.urls import path
from .views import display_items, add_item, delete_item, edit_item

app_name = 'taskmanager'

urlpatterns = [
    path('', display_items, name='display_items'),
    path('add/', add_item, name='add_item'),
    path('edit/<int:item_id>/', edit_item, name='edit_item'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]