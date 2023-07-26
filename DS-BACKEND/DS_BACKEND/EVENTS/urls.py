from django.urls import path
from . import views

urlpatterns=[
    path('api/events/', views.api_event_list, name="event_api"),
    path('api/event/<int:event_id>/',
         views.api_get_one_event, name="one_event_api"),
    path('api/all_events/', views.api_all_events, name="all_events"),
    path('api/past_events/', views.api_past_events, name="past_events"),
    path('api/live_events/', views.api_live_events, name="live_events"),
    path('api/upcoming_events/', views.api_upcoming_events, name="upcoming_events"),
]