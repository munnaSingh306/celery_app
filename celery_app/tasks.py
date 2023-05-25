from mcelery.celery import app
from logging import getLogger
from datetime import datetime
from celery import shared_task

logger = getLogger(__name__)


@app.task
def check_celery_task():
    for i in range(10):
        logger.info(f"----------->{i}")


@app.task
def add(x, y):
    z = x + y
    logger.info(msg=f"{datetime.now()}, Task add:, {x, y, z}")


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'add',
        'schedule': 3.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'Asia/Kolkata'


@shared_task
def scheduel_task(a, b):
    logger.info(msg=f"{datetime.now()}, Task add: {a, b}")
    return None
