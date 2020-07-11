from __future__ import absolute_import, unicode_literals

import requests

from webscraper.celery import app
from scraper.models import ScrapedUrl
from scraper.html_filters import example_html_filter


@app.task(bind=True)
def scrap_url(self, pk: int, url: str):
    status = self.AsyncResult(self.request.id).state
    ScrapedUrl.objects.filter(id=pk).update(task_status=status)

    html_text = requests.get(url).text
    html_text = example_html_filter(html_text)
    ScrapedUrl.objects.filter(id=pk).update(data=html_text)

    ScrapedUrl.objects.filter(id=pk).update(task_status='SUCCESS')
