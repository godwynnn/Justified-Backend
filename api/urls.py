from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SermonViewSet, EventViewSet, LeaderViewSet, ContactMessageViewSet, ServiceViewSet
from .auth_views import signup, login

router = DefaultRouter()
router.register(r'sermons', SermonViewSet)
router.register(r'events', EventViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'contact', ContactMessageViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('', include(router.urls)),
]
