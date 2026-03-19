from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SermonViewSet, EventViewSet, LeaderViewSet, ContactMessageViewSet
from .auth_views import signup, login

router = DefaultRouter()
router.register(r'sermons', SermonViewSet)
router.register(r'events', EventViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'contact', ContactMessageViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('', include(router.urls)),
]
