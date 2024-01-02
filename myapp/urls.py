from django.urls import path

from myapp.views import index_view
from myapp.views.sample_view import SampleView

urlpatterns = [
    path('index', index_view.index, name='index'),
    path('sample', SampleView.as_view(), name='sample'),
]
