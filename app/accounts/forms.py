from django.utils.translation import ugettext_lazy as _

import account.forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import FormActions, StrictButton

class LoginForm(account.forms.LoginUsernameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper = FormHelper()
        helper.form_id = 'login-form'
        helper.form_method = 'post'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-4'
        helper.field_class = 'col-lg-7'
        helper.layout = Layout(
            'username',
            'password',
            # 'remember',
            Div(Div(StrictButton(_('Log in'), css_class='btn-primary',
                                 type='submit'),
                    css_class='col-lg-offset-4 col-lg-7'),
                css_class='form-group')
        )

class SignupForm(account.forms.SignupForm):
    email = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper = FormHelper()
        helper.form_id = 'signup-form'
        helper.form_method = 'post'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-4'
        helper.field_class = 'col-lg-7'
        helper.layout = Layout(
            'username',
            'password',
            'password_confirm',
            # 'email',
            Div(Div(StrictButton(_('Sign up'), css_class='btn-primary',
                                 type='submit'),
                    css_class='col-lg-offset-4 col-lg-7'),
                css_class='form-group')
        )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['email'] = 'none@localhost'

        return cleaned_data
