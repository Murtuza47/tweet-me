from django.db import models
from django.conf import settings

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTHOR_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=true, blank=true)

    def __str__(self):
        return self.content[:80] + "......."

