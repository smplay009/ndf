import os
import sys
import traceback

# مسیر پروژه رو اضافه کن
sys.path.insert(0, '/home/remedybyir/ndf/mydjango')

# تنظیمات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    with open("/home/remedybyir/ndf/logs/wsgi_error.log", "w") as f:
        f.write(traceback.format_exc())
    raise
