from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *

@api_view(['GET'])
def DSmembersOverview(request):
    members_urls = {
        'current-members' : '/api/members/current-members/',
        'alumni' : '/api/members/alumni/',
    # 'all-members' : '/api/members/all-members/<str:pk>/',
        'sophomores' : '/api/members/sophomores/',
        'pre-final-years' : '/api/members/pre-final-years/',
        'final-years' : '/api/members/final-years/',
    }
    return JsonResponse(members_urls)

@api_view(['GET'])
def get_current_members(request):
    members = Member.objects.exclude(current_year = "NA").order_by('firstname')
    serializer = MemberSerializer(members, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_alumni(request):
    alums = Member.objects.filter(current_year = "NA").order_by('firstname')
    serializer = MemberSerializer(alums, many = True)
    return JsonResponse(serializer.data,safe=False)

# @api_view(['GET'])
# def get_all_members(request):
   

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
    
