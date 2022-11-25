"""UserProfile/Views"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from .forms import UserProfileForm


class ProfileView(LoginRequiredMixin, UpdateView):
    """User profile modification view"""

    form_class = UserProfileForm
    template_name = "account/userprofilepage.html"

    def get_object(self, queryset=None):
        """Override default object to return user object"""
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None

        return user

    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated.")
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was a problem with your profile. Please try again."
        )
        return super().form_invalid(form)
