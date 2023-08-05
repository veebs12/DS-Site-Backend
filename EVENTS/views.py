from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from django.http import JsonResponse, Http404
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
    events_past = event.objects.filter(active=True, event_starttime__lt=datetime.now(), event_endtime__lt=datetime.now())

    return JsonResponse({
        'upcoming': EventSerializer(events_upcoming, many=True).data,
        'live': EventSerializer(events_live, many=True).data,
        'past':EventSerializer(events_past,many=True).data,
        'all': EventSerializer(events_all, many=True).data
    }, safe=False)

@api_view(['GET'])
def api_all_events(request):
    events_all = event.objects.filter(active=True).order_by('-event_datetime')

    return JsonResponse({'all': EventSerializer(events_all, many=True).data})

@api_view(['GET'])
def api_past_events(request):
    events_past = event.objects.filter(active=True, event_starttime__lt=datetime.now(), event_endtime__lt=datetime.now())
    

    return JsonResponse({'past':EventSerializer(events_past,many=True).data})

@api_view(['GET'])
def api_live_events(request):
    events_live = event.objects.filter(active=True, event_starttime__lt=datetime.now(
    ), event_endtime__gt=datetime.now()).order_by('-event_datetime')
    

    return JsonResponse({'live': EventSerializer(events_live, many=True).data})

@api_view(['GET'])
def api_upcoming_events(request):
    events_upcoming = event.objects.filter(active=True,
                                           event_starttime__gt=datetime.now(),
                                           event_starttime__lt=datetime.now() + timedelta(days=15)
                                           ).order_by('-event_datetime')
    

    return JsonResponse({'upcoming': EventSerializer(events_upcoming, many=True).data})


@api_view(['GET'])
def api_get_one_event(request, event_id):
    try:
        _event = event.objects.get(id=event_id)

        return JsonResponse(EventSerializer(_event).data)
    
    except Http404:
        return JsonResponse({"error": "Event not found."}, status=404)




# Create your views here.
