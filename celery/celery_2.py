from celery import Celery

app = Celery('tasks', broker='amqp://localhost//', backend = 'db+sqlite:///celery_2.sqlite3')
# CELERY_RESULT_BACKEND = "database"
# CELERY_RESULT_DBURI   = "sqlite:///celery_2.sqlite"

@app.task
def reverse(string):
    return string[::-1]

# Running it...
# >>> from selery_2 import *
# >>> x = reverse.delay('hello world')
# >>> x.status