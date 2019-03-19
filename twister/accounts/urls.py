"""Accounts URL Config"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path(
        route='login',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout',
        view=LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='update/<int:pk>',
        view=views.ProfileUpdateView.as_view(),
        name='update'
    ),
]
