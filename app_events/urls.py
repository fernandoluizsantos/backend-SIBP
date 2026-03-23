from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_events.views import EventTypeViewSet, EventViewSet

router = DefaultRouter()
router.register(r"event-types", EventTypeViewSet, basename="event-type")
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("", include(router.urls)),
]
