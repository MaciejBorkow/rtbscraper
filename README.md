# rtbscraper

## About
The rtbscraper web service scraps an HTML of a given URL and saves it to db(Postgres) as text. RestAPI is hosted by Django server, scrapping tasks are delegated to message broker(Redis) and executed by Celery workers.  

## Getting Started

### Prerequisites

- docker
- docker-compose

Software was tested on Ubuntu 20.04


### Installation

1. Download the repository.
1. Run `docker-compose up -d --build`

### API interface

* GET `/scrapped_url/` - return a list of all scraped URLs.
* GET `/scrapped_url/<id:int>` - return the `<id:int>` scraped URL. JSON example:
```json
{
    "id": 1,
    "task_status": "SUCCESS",
    "url": "https://requests.readthedocs.io/en/master/",
    "data": "random data "
}
```

**id** - task token

**task_status** - standard [Celery statuses](https://docs.celeryproject.org/en/master/reference/celery.states.html).

**url** - scrapped URL

**data** - scraped HTML as text

- POST `/scrapped_url/` - start a scrapping task for a given URL. JSON body schema:
```json
{
     "url": "https://requests.readthedocs.io/en/master/"
}
```
