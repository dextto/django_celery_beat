from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class SampleView(APIView):
    def get(self, request):
        return JsonResponse(
            {'sample': 'sample'},
            status=status.HTTP_200_OK,
        )
