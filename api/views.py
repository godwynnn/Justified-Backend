from rest_framework import viewsets, permissions
from .models import Sermon, Event, Leader, ContactMessage, Service
from .serializers import SermonSerializer, EventSerializer, LeaderSerializer, ContactMessageSerializer, ServiceSerializer
from .cloudinary_utils import upload_to_cloudinary

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        self._handle_file_uploads(serializer)
        serializer.save()

    def perform_update(self, serializer):
        self._handle_file_uploads(serializer)
        serializer.save()

    def _handle_file_uploads(self, serializer):
        # Extract files from request
        image_file = self.request.FILES.get('image_file')
        video_file = self.request.FILES.get('video_file')
        audio_file = self.request.FILES.get('audio_file')

        if image_file:
            upload_res = upload_to_cloudinary(image_file, resource_type='image', folder='sermons/thumbnails')
            serializer.validated_data['image_url'] = upload_res.get('url')
        
        if video_file:
            upload_res = upload_to_cloudinary(video_file, resource_type='video', folder='sermons/videos')
            serializer.validated_data['video_url'] = upload_res.get('url')

        if audio_file:
            upload_res = upload_to_cloudinary(audio_file, resource_type='video', folder='sermons/audio')
            serializer.validated_data['audio_url'] = upload_res.get('url')

        # Remove the file objects from validated_data so they don't cause a TypeError in the model constructor
        serializer.validated_data.pop('image_file', None)
        serializer.validated_data.pop('video_file', None)
        serializer.validated_data.pop('audio_file', None)

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all().order_by('time')
    serializer_class = EventSerializer

class LeaderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leader.objects.all().order_by('order')
    serializer_class = LeaderSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
