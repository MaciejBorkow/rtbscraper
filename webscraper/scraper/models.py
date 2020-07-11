from django.db import models


class ScrapedUrl(models.Model):
    task_id = models.CharField(max_length=50, blank=True, default='')
    task_status = models.CharField(max_length=10, blank=True, default='')
    url = models.fields.URLField()
    data = models.fields.TextField(blank=True, default='')
