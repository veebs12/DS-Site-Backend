from django.urls import path
from . import views

urlpatterns = [
    path('api/members/', views.DSmembersOverview, name="DS-members-overview"),
    path('api/members/current-members/', views.get_current_members, name="current_members"),
    path('api/members/alumni/', views.get_alumni, name="alumni"),
    path('api/members/all-members/<int:passout_yr>/', views.get_all_members, name="all-members"),
    path('api/members/sophomores/', views.get_sophomores, name="sophomores"),
    path('api/members/pre-final-years/', views.get_pre_final_years, name="pre-final-years"),
    path('api/members/final-years/', views.get_final_years, name="final-years"),
  ]