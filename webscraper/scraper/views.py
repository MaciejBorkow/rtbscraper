from rest_framework import viewsets
from scraper.serializers import ScrapedUrlSerializer
from scraper.models import ScrapedUrl


class ScrappedUrlViewSet(viewsets.ModelViewSet):
    queryset = ScrapedUrl.objects.all()
    serializer_class = ScrapedUrlSerializer


