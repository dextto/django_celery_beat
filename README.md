Sample programs for Python

# Requirements
- python
- rabbitmq or sqs
- eventlet for Windows

# Samples
1. django + celery
2. Validator using Pydantic
    - @validate_path_params
    - @validate_query_params
    - @validate_body
    - @validate_form_data

# How to run Django
### Create virtual environment and install packages
```
$ poetry shell
$ poetry install
```

### DB migration
```
$ python manage.py migrate
```

### Run Django
```
$ python manage.py runserver 3000
```

# How to run Broker
### Run SQS (localstack)
```
$ docker run -d --rm -it \
  -p 4566:4566 \
  -p 4571:4571 \
  -e SERVICES=s3,sqs \
  -e LOCALSTACK_HOSTNAME="localhost" \
  -e HOSTNAME_EXTERNAL="localhost" \
  -e AWS_ACCESS_KEY_ID=test \
  -e AWS_SECRET_ACCESS_KEY=test \
  localstack/localstack
```

### Create queue
```
sqs create-queue --queue-name celery-queue
```

OR

### Run RabbitMQ
```
$ docker run -d --hostname my-rabbit --name my-rabbit -e RABBITMQ_DEFAULT_USER=test -e RABBITMQ_DEFAULT_PASS=test -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

# How to run celery and beat
### Run celery on terminal 1
`-P eventlet` option is needed for Windows.
```
$ celery -A proj worker -l info -P eventlet
```

### Run beat on terminal 2
```
$ celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
