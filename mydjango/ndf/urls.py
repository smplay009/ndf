from django.urls import path
from .views import RatingAPIView

urlpatterns = [
    path("api/rating/", RatingAPIView.as_view(), name="rating"),
]
