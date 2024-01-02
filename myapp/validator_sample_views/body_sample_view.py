from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView

from pydantic import BaseModel, Field

from common.validators import validate_body


class BodySampleView(APIView):

    class CreatePostBody(BaseModel):
        title: str = Field(min_length=1, max_length=20)
        contents: str = Field(min_length=1, max_length=100)

    @validate_body(CreatePostBody)
    def get(
        self,
        request: HttpRequest,
        body: CreatePostBody,
    ):
        return JsonResponse(
            {
                "title": body.title,
                "contents": body.contents,
            },
        )
