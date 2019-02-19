"""Dashboard URL configuration"""

from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        route='',
        view=TemplateView.as_view(template_name='posts/index.html'),
        name='index'
    ),
]