from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *

@api_view(['GET'])
def DSmembersOverview(request):
    members_urls = {
        'current-members' : '/current-members/',
        'alumni' : '/alumni/',
        'all-members' : '/all-members/',
        'sophomores' : '/sophmores/',
        'pre-final-years' : '/pre-final-years/',
        'final-years' : '/final-years/',
    }
    return JsonResponse(members_urls)

@api_view(['GET'])
def get_current_members(request):
    members = Member.objects.all().order_by('firstname')
    serializer = MemberSerializer(members, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_alumni(request):
    alums = Alum.objects.all().order_by('firstname')
    serializer = AlumniSerializer(alums, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_all_members(request):
    pass


@api_view(['GET'])
def get_sophomores(request):
    member2 = Member.objects.filter(passout_year="2026").order_by('firstname')
    return JsonResponse(MemberSerializer(member2, many=True).data, safe=False)

@api_view(['GET'])
def get_pre_final_years(request):
    member3 = Member.objects.filter(passout_year="2025").order_by('firstname')
    return JsonResponse(MemberSerializer(member3, many=True).data, safe=False)
  
@api_view(['GET'])
def get_final_years(request):
    member4 = Member.objects.filter(passout_year="2024").order_by('firstname')
    return JsonResponse(MemberSerializer(member4, many=True).data, safe=False)
    
