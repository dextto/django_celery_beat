from django.urls import path

from myapp.views import index_view
from myapp.views.sample_view import SampleView
from myapp.views.path_param_sample_view import PathParamSampleView

urlpatterns = [
    path('index', index_view.index, name='index'),
    path('path-param-sample/<str:id>', PathParamSampleView.as_view(), name='path-param-sample'),
    path('sample', SampleView.as_view(), name='sample'),
]
