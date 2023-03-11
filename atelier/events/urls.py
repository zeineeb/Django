from .views import *
from django.urls import path

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events"),
     path('addEvent/', add_event ,name="add_event"),
     path('eventslistView/' , ListEventView.as_view(),name='list_events_view') ,
     path('eventDetails/<int:pk>',DetailEventView.as_view(),name='event_details'),
     path('createform/', create_event, name='create_form'),
     path('eventsCreateView/', CreateEvent.as_view(), name='create_event_form'),
     path('eventsUpdateView/<int:pk>', UpdateEvent.as_view(), name= 'update_event_form'),
     path('eventsDeleteView/<int:pk>', DeleteEvent.as_view(), name= 'delete_event'),
     path('participateView/<int:eventId>', participate, name= 'participate'),
]
