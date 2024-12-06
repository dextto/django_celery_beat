# coding=utf-8

from __future__ import absolute_import

from celery import Celery


# django 에서 쓰일 setting 지정 아래의 경우 proj/settings.py 를 사용한다는 뜻
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
from django.conf import settings  # noqa

app = Celery(
    "proj",
    broker="amqp://guest@localhost//",
    # backend="django-db",  # DB에 결과 저장
)

# Optional configuration, see the application user guide.

# django.conf:settings 로 django setting 을 celery 의 config 로 불러온다.
app.config_from_object("django.conf:settings", namespace="CELERY")
# INSTALLED_APPS 안에 있는 tasks.py 들을 알아서 import 해 준다.
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.update(
    worker_concurrency=10,  # 워커의 병렬 처리 수
    # CELERY_TASK_RESULT_EXPIRES=3600,
)

app.conf.beat_schedule = {
    "add-every-3-seconds": {
        "task": "proj.tasks.add",
        "schedule": 3.0,
        "args": (16, 16),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


if __name__ == "__main__":
    app.start()
