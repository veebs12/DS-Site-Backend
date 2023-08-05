from rest_framework import serializers
from .models import event as Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
