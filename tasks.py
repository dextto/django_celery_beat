from celery import Celery

# app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')
app = Celery('tasks',
        broker = 'amqp://guest:guest@localhost:5672//',
        backend = 'amqp://',
        )

@app.task
def add(x,y):
    return x+y