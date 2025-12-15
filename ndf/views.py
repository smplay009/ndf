from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating

@method_decorator(csrf_exempt, name='dispatch')
class RatingAPIView(APIView):
    def post(self, request):
        # گرفتن دیتا از JSON
        data = request.data
        rating = Rating.objects.create(
            q1=int(data.get("q1", 0)),
            q2=int(data.get("q2", 0)),
            q3=int(data.get("q3", 0)),
            q4=int(data.get("q4", 0)),
            q5=int(data.get("q5", 0)),
        )
        return Response({
            "status": "success",
            "total_score": rating.total_score,
            "average_score": rating.average_score
        })
