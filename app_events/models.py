from django.db import models
from app_base.mixins import AuditMixin

class EventType(models.Model):
    name = models.CharField(max_length=100)

class Event(AuditMixin):
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)      
    event_image_BASE64 = models.TextField()    
    

