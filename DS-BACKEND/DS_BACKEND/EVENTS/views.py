from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import event
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def api_event_list(request):
    events_all = event.objects.filter(active=True).order_by('-event_datetime')
    events_upcoming = event.objects.filter(active=True,
                                           event_starttime__gt=datetime.now(),
                                           event_starttime__lt=datetime.now() + timedelta(days=15)
                                           ).order_by('-event_datetime')
    events_live = event.objects.filter(active=True, event_starttime__lt=datetime.now(
    ), event_endtime__gt=datetime.now()).order_by('-event_datetime')
    events_past = event.objects.filter(active=False, event_starttime__lt=datetime.now(), event_endtime__lt=datetime.now())

    return JsonResponse({
        'upcoming': EventSerializer(events_upcoming, many=True).data,
        'live': EventSerializer(events_live, many=True).data,
        'past':EventSerializer(events_past,many=True).data,
        'all': EventSerializer(events_all, many=True).data
    }, safe=False)




# Create your views here.
