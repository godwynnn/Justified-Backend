from rest_framework import serializers
from .models import Sermon, Event, Leader, ContactMessage

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
