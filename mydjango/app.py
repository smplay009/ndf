import os
import sys

# مسیر اصلی پروژه Django
BASE_DIR = os.path.join(os.path.dirname(__file__), 'mydjango')
sys.path.insert(0, BASE_DIR)

# تنظیمات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

# WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

