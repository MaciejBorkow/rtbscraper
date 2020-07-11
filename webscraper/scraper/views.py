from rest_framework import viewsets
from scraper.serializers import ScrapedUrlSerializer
from scraper.tasks import scrap_url
from scraper.models import ScrapedUrl


class ScrappedUrlViewSet(viewsets.ModelViewSet):
    queryset = ScrapedUrl.objects.all()
    serializer_class = ScrapedUrlSerializer

    def perform_create(self, serializer):
        serializer.save()
        celery_task = scrap_url.delay(serializer.instance.id)
        serializer.instance.task_status = celery_task.status
        serializer.instance.task_id = celery_task.id
        serializer.instance.save()
