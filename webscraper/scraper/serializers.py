from rest_framework import serializers
from scraper.models import ScrapedUrl


class ScrapedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedUrl
        fields = ['id', 'task_status', 'url', 'data']
        read_only_fields = ['task_status', 'data']
