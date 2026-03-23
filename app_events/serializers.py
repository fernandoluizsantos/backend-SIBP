from rest_framework import serializers

from app_events.models import Event, EventType


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ["id", "name"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "type",
            "title",
            "description",
            "initial_date",
            "final_date",
            "is_repeated",
            "event_image_BASE64",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, attrs):
        initial_date = attrs.get("initial_date")
        final_date = attrs.get("final_date")

        if self.instance:
            initial_date = initial_date or self.instance.initial_date
            final_date = final_date or self.instance.final_date

        if initial_date and final_date and final_date < initial_date:
            raise serializers.ValidationError(
                {"final_date": "A data final deve ser maior ou igual a data inicial."}
            )

        return attrs
