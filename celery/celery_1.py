# Requirements
# 1. rabbitmq-server
#       -> $ sudo apt install rabbitmq-server
#       -> $ sudo service rabbitmq-server restart
#       -> $ sudo rabbitmqctl status
# 2. Celery
#       -> pip3 install celery --user

# Simple app to run it from command line

from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')

@app.task
def reverse(string):
    return string[::-1]

# Now, run celery monitor from the command line
#       -> $ celery -A celery_1(appname) worker --loglevel=info

# terminal-1 : $ celery -A celery_1 worker --loglevel=info
# terminal-2 : >>> from celery_1 import reverse
#              >>> reverse('Hello there...') #This will run the fucntion as it is.
#              >>> reverse.delay('Hello there...')# This is run the function with background task.