from django.http import JsonResponse
from rest_framework.views import APIView

from proj.tasks import add


class CeleryTestView(APIView):
    def get(self, request):

        result = add.delay(4, 6)

        return JsonResponse({"task_id": result.id, "result": result.get()})
