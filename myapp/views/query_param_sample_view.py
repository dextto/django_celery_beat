from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView

from pydantic import BaseModel, Field

from common.validators import validate_query_params


class QueryParamSampleView(APIView):

    class Paging(BaseModel):
        page: int = Field(default=1, ge=1)
        page_size: int = Field(default=10, ge=1)

    @validate_query_params(Paging)
    def get(
        self,
        request: HttpRequest,
        params: Paging,
    ):
        return JsonResponse(
            {
                "page": params.page,
                "page_size": params.page_size,
            },
        )
