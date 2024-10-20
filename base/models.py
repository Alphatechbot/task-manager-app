from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import MyUser


# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base:update', kwargs={'id': self.id})

    def get_absolute_url1(self):
        return reverse('base:delete', kwargs={'id': self.id})
