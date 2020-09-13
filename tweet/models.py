from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        if self.content.__len__() <= 80:
            return self.content
        return self.content[:80] + "......."


    @property
    def update_tweet_time(self):
        self.update_date = datetime.now()
        return self.update_date
