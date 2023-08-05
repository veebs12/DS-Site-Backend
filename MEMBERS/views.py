from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.utils import timezone as tz

def get_current_batch():
    date = tz.now()
    if date.month > 6:
        return date.year + 1
    return date.year

@api_view(['GET'])
def DSmembersOverview(request):
    members_urls = {
        'current-members' : '/api/members/current-members/',
        'alumni' : '/api/members/alumni/',
        'all-members' : '/api/members/all-members/<int:passout_yr>/',
        'sophomores' : '/api/members/sophomores/',
        'pre-final-years' : '/api/members/pre-final-years/',
        'final-years' : '/api/members/final-years/',
    }
    return JsonResponse(members_urls)

@api_view(['GET'])
def get_current_members(request):
    year = get_current_batch()
    members = Member.objects.filter(passout_year__gte=year).order_by('firstname')
    serializer = MemberSerializer(members, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_alumni(request):
    year = get_current_batch()
    alums = Member.objects.filter(passout_year__lt=year).order_by('firstname')
    serializer = MemberSerializer(alums, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_all_members(request,passout_yr):
    passout = Member.objects.filter(passout_year=passout_yr)
    serializer = MemberSerializer(passout, many = True)
    return JsonResponse(serializer.data,safe=False)  

@api_view(['GET'])
def get_sophomores(request):
    year = get_current_batch()
    member2 = Member.objects.filter(passout_year=year+2).order_by('firstname')
    return JsonResponse(MemberSerializer(member2, many=True).data, safe=False)

@api_view(['GET'])
def get_pre_final_years(request):
    year = get_current_batch()
    member3 = Member.objects.filter(passout_year=year+1).order_by('firstname')
    return JsonResponse(MemberSerializer(member3, many=True).data, safe=False)

@api_view(['GET'])
def get_final_years(request):
    year = get_current_batch()
    member4 = Member.objects.filter(passout_year=year).order_by('firstname')
    return JsonResponse(MemberSerializer(member4, many=True).data, safe=False)

