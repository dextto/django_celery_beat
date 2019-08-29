Run a celery a task with celery, django and beat.

I've tested on Windows 7. On Linux, it would be similar. :)
Python 3.5.4 + Celery 4.2.1 + Django 2.1.2

1. Install python & rabbitmq
2. Make you virtural evironment
3. Install celery & django using pip
4. Install eventlet to check result. This is for Windows env.
5. add a queue on rabittmq named "TEST" 
6. run celery:
    ```
    proj$ celery -A proj worker -l info -P eventlet
    ```
7. run beat: proj> celery -A proj beat -l info
    ```
    proj$ celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```
