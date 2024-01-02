import copy
from functools import wraps
from typing import Type

from django.http import JsonResponse
from pydantic import BaseModel, validate_model
from rest_framework import status
from rest_framework.parsers import JSONParser


def validate_path_params(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            _, error_details = validate(model, kwargs)
            if error_details:
                return JsonResponse(
                    data={"details": error_details},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return f(*args, **kwargs)

        return wrapper

    return decorated_func


def validate_query_params(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[1]
            params = request.GET.dict()
            dictStrAny, error_details = validate(model, params)
            if error_details:
                return JsonResponse(
                    data={"details": error_details},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            validated_params = model.construct(**dictStrAny)
            return f(*args, **kwargs, params=validated_params)

        return wrapper

    return decorated_func


def validate_body(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[1]
            body = JSONParser().parse(request)
            dictStrAny, error_details = validate(model, body)
            if error_details:
                return JsonResponse(
                    data={"details": error_details},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            validated_body = model.construct(**dictStrAny)
            return f(*args, **kwargs, body=validated_body)

        return wrapper

    return decorated_func


def validate_form_data(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[1]

            form_data = copy.deepcopy(request.POST)
            form_data.update(request.FILES)
            dictStrAny, error_details = validate(model, form_data)
            if error_details:
                return JsonResponse(
                    data={"details": error_details},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            validated_form_data = model.construct(**dictStrAny)
            return f(*args, **kwargs, form_data=validated_form_data)

        return wrapper

    return decorated_func


def validate(model: Type[BaseModel], data: dict):
    values, _, validation_error = validate_model(model, data)
    error_details = []
    if validation_error:
        for error in validation_error.errors():
            error_details.append(
                {
                    "field": error["loc"][0],
                    "message": error["msg"],
                }
            )

    return values, error_details
