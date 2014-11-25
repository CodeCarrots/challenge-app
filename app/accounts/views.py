from . import forms
import account.views

# Create your views here.

class LoginView(account.views.LoginView):
    form_class = forms.LoginForm


class SignupView(account.views.SignupView):
    form_class = forms.SignupForm
