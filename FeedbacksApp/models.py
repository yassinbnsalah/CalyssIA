# In FeedbacksApp/models.py
from django.db import models
from django.utils import timezone

from UserApp.models import RUser

class Feedback(models.Model):
    prevention = models.ForeignKey(
        'PreventionApp.Prevention', 
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    content = models.TextField()
    rating = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(RUser , on_delete= models.CASCADE , null=True)
    def __str__(self):
        return f'Feedback for {self.prevention.title} (Anonymous)'
