import copy
from functools import wraps
from typing import Type

from django.http import JsonResponse
from pydantic import BaseModel
from rest_framework import status
from rest_framework.parsers import JSONParser


def validate_path_params(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(request, *args, **kwargs):
            try:
                params = model(**kwargs)
                return f(request, params=params, *args)
            except ValueError as e:
                return JsonResponse(
                    data={"details": e.errors()},
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
            try:
                validated_params = model.model_validate(params)
            except ValueError as e:
                return JsonResponse(
                    data={"details": e.errors()},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return f(*args, **kwargs, params=validated_params)

        return wrapper

    return decorated_func


def validate_body(model: Type[BaseModel]):
    def decorated_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[1]
            body = JSONParser().parse(request)
            try:
                validated_body = model.model_validate(body)
            except ValueError as e:
                return JsonResponse(
                    data={"details": e.errors()},
                    status=status.HTTP_400_BAD_REQUEST,
                )

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
            try:
                validated_form_data = model.model_validate(form_data)
            except ValueError as e:
                return JsonResponse(
                    data={"details": e.errors()},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return f(*args, **kwargs, form_data=validated_form_data)

        return wrapper

    return decorated_func
