from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MEMBERS.urls'))
    path('mainEVENTS/', include('EVENTS.urls')),
]
