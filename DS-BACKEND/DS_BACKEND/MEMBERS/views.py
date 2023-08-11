from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .serializers import *
from .forms import *


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
    members = Member.objects.exclude(current_year = "NA").order_by('firstname')
    serializer = MemberSerializer(members, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_alumni(request):
    alums = Member.objects.filter(current_year = "NA").order_by('firstname')
    serializer = MemberSerializer(alums, many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_all_members(request,passout_yr):
    passout = Member.objects.filter(passout_yr=passout_yr)
    serializer = MemberSerializer(passout, many = True)
    return JsonResponse(serializer.data,safe=False)  

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

def members_form(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'members/success.html') 
    else:
        form = MemberCreationForm()

    return render(request, 'members/create_members.html', {'form': form})


    
