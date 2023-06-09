from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.defaults import (
    permission_denied,
    bad_request,
    page_not_found,
    server_error,
)
from django.views.generic import View
from allauth.account.views import SignupView, PasswordChangeView

from jobportal.base_views import RelatedUserRequiredMixin

from .forms import CustomSignupForm, PasswordConfirmationForm


# ___Error Views___


def custom_bad_request_view(
    request, exception, template_name="errors/400.html"
):
    """Override the default bad request view to display custom 400 page
    on specific URL path"""
    return bad_request(request, exception, template_name)


def custom_permission_denied_view(
    request, exception, template_name="errors/403.html"
):
    """Override the default permission denied view to display custom 403 page
    on specific URL path"""
    return permission_denied(request, exception, template_name)


def custom_page_not_found_view(
    request, exception, template_name="errors/404.html"
):
    """Override the default page not found view to display custom 404 page
    on specific URL path"""
    return page_not_found(request, exception, template_name)


def custom_server_error_view(request, template_name="errors/500.html"):
    """Override the default server error view to display custom 500 page
    on specific URL path"""
    return server_error(request, template_name)


# ___Account Views___


class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def dispatch(self, request, *args, **kwargs):
        """Check if role is valid when the user manually set the URL path
        with an invalid role,
        e.g: `/accounts/signup/invalid_role/`,
        then raise 404 error."""
        role = self.kwargs.get("role")
        if role not in self.form_class.Role.values:
            raise Http404
        return super(SignupView, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        """Set the initial value of role field to the value from
        URL parameters."""

        # Get initial data dict from super class
        initial = super().get_initial()

        # Get role from URL parameters
        role = self.kwargs.get("role")
        if role:
            initial["role"] = role
        return initial


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("jobseeker_profile")


class AccountDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """

    def get(self, request, *args, **kwargs):
        """
        Display a confirmation form to the user
        """
        # Pass the user instance to the form
        form = PasswordConfirmationForm(request.user)
        return render(
            request, "account/account_deactivate.html", {"form": form}
        )

    def post(self, request, *args, **kwargs):
        """
        Check if the password is correct and deactivate the user.
        Otherwise, display an error message.
        """
        form = PasswordConfirmationForm(request.user, request.POST)

        if form.is_valid():
            # Set user as inactive and save to database.
            request.user.is_active = False
            request.user.save()

            # Log the user out.
            logout(request)

            # Display success message.
            messages.warning(
                request,
                "Your account has been deactivated"
                " and will be deleted in 30 days.",
            )

            # Redirect to homepage.
            return HttpResponseRedirect("/")

        # Display form with error message.
        return render(
            request, "account/account_deactivate.html", {"form": form}
        )


class EmailNotificationToggle(RelatedUserRequiredMixin, View):
    """Toggle email notification settings"""

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.email_notifications:
            user.email_notifications = False
            user.save()
            success_message = "Email notifications have been disabled"
        else:
            user.email_notifications = True
            user.save()
            success_message = "Email notifications have been enabled"

        return JsonResponse(
            {
                "is_notify_enabled": user.email_notifications,
                "successMsg": success_message,
            }
        )
