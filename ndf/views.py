from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name="dispatch")
class RatingAPIView(APIView):

    def post(self, request):
        answers = request.data.get("answers", {})

        if not answers or not isinstance(answers, dict):
            return Response({"error": "Invalid data"}, status=400)

        rating = Rating.objects.create(answers=answers)

        return Response({
            "status": "success",
            "answers": rating.answers,
            "total_score": rating.total_score,
            "average_score": rating.average_score,
        })
