"""Accounts views"""

from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import SignupForm


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
