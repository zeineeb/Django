
from .Views import *
from django.urls import path

urlpatterns = [
     path('get/', getEvent ,name="get_Event"),
     path('add/', addEvent ,name="add_Event"),
     path('update/<int:id>', updateEvent ,name="update_Event"),
     path('delete/<int:id>', deleteEvent ,name="delete_Event")

]