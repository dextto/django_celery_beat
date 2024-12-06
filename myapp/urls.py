from django.urls import path

from myapp.views import index_view
from myapp.views.celery_test_view import CeleryTestView
from myapp.views.sample_view import SampleView
from myapp.validator_sample_views.path_param_sample_view import PathParamSampleView
from myapp.validator_sample_views.query_param_sample_view import QueryParamSampleView
from myapp.validator_sample_views.body_sample_view import BodySampleView

urlpatterns = [
    path("index", index_view.index, name="index"),
    path(
        "path-param-sample/<str:id>",
        PathParamSampleView.as_view(),
        name="path-param-sample",
    ),
    path(
        "query-param-sample", QueryParamSampleView.as_view(), name="query-param-sample"
    ),
    path("body-sample", BodySampleView.as_view(), name="body-sample"),
    path("sample", SampleView.as_view(), name="sample"),
    path("celery-test", CeleryTestView.as_view(), name="celery-test"),
]
