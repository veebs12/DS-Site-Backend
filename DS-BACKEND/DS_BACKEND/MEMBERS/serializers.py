from rest_framework import serializers
from .models import Member,Alum

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alum
        fields = "__all__"
