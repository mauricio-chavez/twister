"""Dashboard URL configuration"""

from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index'
    ),
]