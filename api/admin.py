from django.contrib import admin
from .models import Sermon, Event, Leader, ContactMessage, Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'day_of_week', 'start_time', 'is_active')
    list_filter = ('service_type', 'day_of_week', 'is_active')

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date')
    search_fields = ('title', 'speaker')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'time', 'is_live_streamed')

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    ordering = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
