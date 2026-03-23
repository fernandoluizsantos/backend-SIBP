from rest_framework import viewsets

from app_events.models import Event, EventType
from app_events.serializers import EventSerializer, EventTypeSerializer


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all().order_by("name")
    serializer_class = EventTypeSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("type").all().order_by("-initial_date")
    serializer_class = EventSerializer
