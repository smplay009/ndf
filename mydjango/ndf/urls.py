from django.contrib import admin  # اینو اضافه کن
from django.urls import path
from django.http import HttpResponse
from .views import RatingAPIView

# view ساده برای مسیر اصلی اپ
def home(request):
    return HttpResponse("NDf app is running!")

urlpatterns = [
    path('admin/', admin.site.urls),       # ادمین اینجا درست میشه
    path("", home, name="home"),           # مسیر root
    path("api/rating/", RatingAPIView.as_view(), name="rating"),  # مسیر API
]

