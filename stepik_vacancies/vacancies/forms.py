from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from django.contrib.auth.forms import UserCreationForm
from .models import Application


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Зарегистривоваться'))


class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Записаться на пробный урок'))

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {'written_username': 'Ваше имя', 'written_phone': 'Ваш номер телефона',
                  'written_cover_letter': 'Ваш отклик'}
