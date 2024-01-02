from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView

from pydantic import BaseModel, Field

from common.validators import validate_path_params


class PathParamSampleView(APIView):

    class Id(BaseModel):
        id: int = Field(gt=0)

    @validate_path_params(Id)
    def get(
        self,
        request: HttpRequest,
        params: Id,
    ):
        return JsonResponse(
            {'path_param_sample': params.id},
        )
