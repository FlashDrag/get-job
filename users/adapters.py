from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

from .forms import CustomSignupForm


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
        """
        Redirect to the profile page of the selected role
        after successful signup
        """

        # Get selected role
        role = request.POST.get('role')
        print("role: ", role)
        if role == CustomSignupForm.Role.JOBSEEKER:
            # TODO: Change to jobseeker profile
            redirect_url = reverse('job_search')
        elif role == CustomSignupForm.Role.EMPLOYER:
            # TODO: Change to employer profile
            redirect_url = reverse('resume_search')
        else:
            return super().get_signup_redirect_url(request)
        print("redirect_url: ", redirect_url)
        return redirect_url

    def get_login_redirect_url(self, request):
        """
        Redirect to the homepage of the selected role
        if no next URL is provided
        """
        if request.user.role == CustomSignupForm.Role.JOBSEEKER:
            return reverse('jobseeker_home')
        elif request.user.role == CustomSignupForm.Role.EMPLOYER:
            return reverse('employer_home')
        else:
            return super().get_login_redirect_url(request)