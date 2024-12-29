from django.db import models
from django.utils import timezone
import uuid

class CustomToken(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', related_name='tokens', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user.username} - {self.key}"

    def is_valid(self):
        return self.is_active and self.expires > timezone.now()

    def invalidate(self):
        self.is_active = False
        self.save()
