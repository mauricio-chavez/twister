"""Accounts views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from .forms import SignupForm
from .models import Profile


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        form.send_info_message(self.request)
        return super().form_valid(form)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view"""

    model = Profile
    template_name = "registration/update.html"
    fields = [
        'display_name',
        'avatar',
        'biography',
        'birthday',
        'location',
        'website',
    ]

