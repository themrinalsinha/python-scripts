# https://mail.google.com/mail/?view=cm&fs=1&to=someone@example.com&su=SUBJECT&body=BODY&bcc=someone.else@example.com

from urllib.parse import urlencode
from webbrowser   import open as open_browser

TO_EMAIL = "themrinalsinha@gmail.com"
SUBJECT  = "My Subject line"
BODY     = "My body line"

url_parameters    = urlencode(dict(view='cm', fs='1', to=TO_EMAIL, su=SUBJECT, body=BODY))
email_compose_url = f"https://mail.google.com/mail/?{url_parameters}"
open_browser(email_compose_url)