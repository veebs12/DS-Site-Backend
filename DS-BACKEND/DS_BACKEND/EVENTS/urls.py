from django.urls import path
from . import views

urlpatterns=[
    path('api/events/', views.api_event_list, name="event_api"),
    path('api/event/<int:event_id>/',
         views.api_get_one_event, name="one_event_api"),
]