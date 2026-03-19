from rest_framework import viewsets, permissions
from .models import Sermon, Event, Leader, ContactMessage
from .serializers import SermonSerializer, EventSerializer, LeaderSerializer, ContactMessageSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all().order_by('time')
    serializer_class = EventSerializer

class LeaderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leader.objects.all().order_by('order')
    serializer_class = LeaderSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
