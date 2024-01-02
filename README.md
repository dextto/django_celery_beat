Sample programs for Python

# Requirements
- python
- rabbitmq
- eventlet for Windows

# Samples
1. django + celery
2. Validator using Pydantic
    - @validate_path_params
    - @validate_query_params
    - @validate_body
    - @validate_form_data

# How to run celery and beat
### run celery
```
proj$ celery -A proj worker -l info -P eventlet
```

### run beat: proj> celery -A proj beat -l info
```
proj$ celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
