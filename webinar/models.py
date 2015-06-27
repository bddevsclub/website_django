from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Webinar(models.Model):
    title = models.CharField("Title", max_length=250)
    date_time = models.DateTimeField("Date & Time")
    video_url = models.URLField("Video URL")
    description = models.TextField("Description")
    embed_code = models.TextField("Video Embed Code")
    tags = TaggableManager()

    def __str__(self):
        return self.title


class FacebookGroup(models.Model):
    name = models.CharField("Name", max_length=250)
    url = models.URLField("URL")
    description = models.TextField("Description")

    def __str__(self):
        return self.name
