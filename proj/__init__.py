from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app


# Version
__version__ = "0.1.0"
__version_info__ = tuple(
    int(num) if num.isdigit() else num
    for num in __version__.replace("-", ".", 1).split(".")
)


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
__all__ = ("celery_app",)
