import os
import sys
import traceback

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, "mydjango"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    with open(os.path.join(BASE_DIR, "stderr.log"), "w") as f:
        f.write(traceback.format_exc())
    raise
