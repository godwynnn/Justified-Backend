from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True)
    notes_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.speaker}"

class Event(models.Model):
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=50) # e.g. "Sunday", "Wednesday"
    time = models.TimeField()
    is_live_streamed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.day}"

class Leader(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255) # e.g. "Senior Pastor"
    bio = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0) # For sorting

    def __str__(self):
        return f"{self.name} - {self.role}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

SERVICE_TYPES = [
    ('worship', 'Worship Service'),
    ('bible_study', 'Bible Study'),
    ('prayer', 'Prayer Session'),
]

class Service(models.Model):
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.day_of_week}"
