from mcelery.celery import app
from logging import getLogger
logger = getLogger(__name__)

@app.task
def check_celery_task():
    for i in range(10):
        logger.info(f"----------->{i}")