from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import StrictButton, FieldWithButtons, InlineField


class SolutionForm(forms.Form):
    code = forms.CharField(label='Rozwiązanie', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper = FormHelper()
        helper.form_id = 'solution-form'
        helper.form_method = 'post'
        helper.form_class = 'form-inline'
        # helper.field_template = 'bootstrap3/layout/inline_field.html'
        # helper.form_class = 'form-horizontal'
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-8'
        submit = StrictButton('Sprawdź!', css_class='btn-primary',
                              type='submit')
        helper.layout = Layout(
            # 'code',
            # submit,
            InlineField('code'),
            # FieldWithButtons('code', submit),
            # FieldWithButtons(InlineField('code'), submit)
        )
