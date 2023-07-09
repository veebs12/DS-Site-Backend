from django.urls import path
from . import views
urlpatterns = [
    path('', views.DSmembersOverview, name="DS-members-overview"),
    path('current-members/', views.get_current_members, name="current_members"),
    path('alumni/', views.get_alumni, name="alumni"),
    path('all-members/', views.get_all_members, name="all-members"),
    path('sophomores/', views.get_sophomores, name="sophomores"),
    path('pre-final-years/', views.get_pre_final_years, name="pre-final-years"),
    path('final-years/', views.get_final_years, name="final-years"),
  ]