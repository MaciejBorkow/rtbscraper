from __future__ import absolute_import, unicode_literals

import requests

from webscraper.celery import app
from scraper.models import ScrapedUrl
from scraper.html_filters import example_html_filter


def state_up_to_date(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        pk = kwargs['pk']
        status = self.AsyncResult(self.request.id).state
        ScrapedUrl.objects.filter(id=pk).update(task_status=status)
        func(*args, **kwargs)
        ScrapedUrl.objects.filter(id=pk).update(task_status='SUCCESS')
    return wrapper


@app.task(bind=True)
@state_up_to_date
def scrap_url(self, *, pk: int, url: str):
    html_text = requests.get(url).text
    html_text = example_html_filter(html_text)
    ScrapedUrl.objects.filter(id=pk).update(data=html_text)
