from celery    import Celery
from requests  import Session
from lxml.html import fromstring

app = Celery('tasks', broker='amqp://localhost//', backend = 'db+sqlite:///dj_test.sqlite3')

@app.task
def fetch(string):
    s    = Session()
    html = s.get('https://django-test.advarisk.com')
    root = fromstring(html.text)
    csrf = root.xpath('/html/body/form/input/@value')[0]
    html = s.post('https://django-test.advarisk.com', data = {'csrf_token' : csrf, 'question' : string})
    root = fromstring(html.text)
    return root.xpath('/html/body/form/p//code/text()')[0]