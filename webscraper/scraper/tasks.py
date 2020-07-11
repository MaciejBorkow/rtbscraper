from __future__ import absolute_import, unicode_literals

from scraper.models import ScrapedUrl
from webscraper.celery import app


@app.task(bind=True)
def scrap_url(self, id):
    status = self.AsyncResult(self.request.id).state
    ScrapedUrl.objects.filter(id=id).update(task_status=status)
    ScrapedUrl.objects.filter(id=id).update(data='maciej')
    ScrapedUrl.objects.filter(id=id).update(task_status='SUCCESS')
