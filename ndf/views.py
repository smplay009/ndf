from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating

class RatingAPIView(APIView):
    def post(self, request):
        rating = Rating.objects.create(
            q1=int(request.data.get("q1", 0)),
            q2=int(request.data.get("q2", 0)),
            q3=int(request.data.get("q3", 0)),
            q4=int(request.data.get("q4", 0)),
            q5=int(request.data.get("q5", 0)),
        )

        return Response({
            "status": "success",
            "total_score": rating.total_score,
            "average_score": rating.average_score
        })
