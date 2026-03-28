from rest_framework import serializers
from .models import Sermon, Event, Leader, ContactMessage, Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class SermonSerializer(serializers.ModelSerializer):
    image_file = serializers.FileField(write_only=True, required=False)
    video_file = serializers.FileField(write_only=True, required=False)
    audio_file = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'speaker', 'date', 'description', 
            'image_url', 'video_url', 'audio_url', 'notes_url', 
            'created_at', 'image_file', 'video_file', 'audio_file'
        ]
        read_only_fields = ['image_url', 'video_url', 'audio_url', 'created_at']

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
