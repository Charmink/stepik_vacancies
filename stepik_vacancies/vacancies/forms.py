from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, ButtonHolder, Field
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from .models import Application, Company, Vacancy, Resume


class MyUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(ButtonHolder(
            Fieldset('', 'username', 'first_name', 'last_name', 'password'),
            Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block')))

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        labels = {'username': 'Логин', 'first_name': 'Имя', 'last_name': 'Фамилия',
                  'password': 'Пароль'}
        widget = {
            'username': forms.TextInput(attrs={'type': "text", 'id': "inputLogin", 'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'type': "text", 'id': "inputName", 'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'type': "text", 'id': "inputSurname", 'class': "form-control"}),
            'password': forms.TextInput(attrs={'type': "password", 'id': "inputPassword", 'class': "form-control"})
        }


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(ButtonHolder(Fieldset('', 'username', 'password'),
                                                 Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block')))


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


class MyCompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout =\
            Layout(ButtonHolder(Fieldset('', 'name', 'logo', 'employee_count',
                                         'location', 'description'),
                                Submit('submit', 'Сохранить', css_class='btn btn-info')))

    class Meta:
        model = Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description']
        labels = {'name': 'Название компании', 'logo': 'Логотип',
                  'employee_count': 'Колличество человек в компании', 'location': 'География',
                  'description': 'Информация о компании'}
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "companyName"}),
            'logo': forms.FileInput(attrs={'type': "file", 'class': "custom-file-input", 'id': "inputGroupFile01"}),
            'employee_count': forms.NumberInput(attrs={'class': "form-control", 'type': "number",  'id': "companyTeam"}),
            'location': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'id': "companyLocation"}),
            'description': forms.Textarea(attrs={'class': "form-control", 'rows': "4", 'id': "companyInfo", 'style': "color:#000;"}),
        }


class MyVacancyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = \
            Layout(ButtonHolder(Fieldset('', 'title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description'),
                                Submit('submit', 'Сохранить', css_class='btn btn-info')))

    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
        labels = {'title': 'Название вакансии', 'specialty': 'Специализация',
                  'salary_min': 'Зарплата от', 'salary_max': 'Зарплата до',
                  'skills': 'Требуемые навыки', 'description': 'Описание вакансии'}
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'type': "text",
                                            'id':"vacancyTitle"}),

            'specialty': forms.Select(attrs={'class': "custom-select mr-sm-2",
                                             'id': "userSpecialization"}),
            'salary_min': forms.NumberInput(attrs={'class': "form-control", 'type': "text",
                                                   'id': "vacancySalaryMin"}),
            'salary_max': forms.NumberInput(attrs={'class': "form-control", 'type': "text",
                                                   'id': "vacancySalaryMax"}),
            'skills': forms.Textarea(attrs={'class': "form-control", 'rows': '3',
                                            'id': "vacancySkills", 'style': "color:#000;"}),
            'description': forms.Textarea(attrs={'class': "form-control", 'rows': "13",
                                                 'id': "vacancyDescription",
                                                 'style': "color:#000;"})

        }


class MyResumeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(ButtonHolder(
            Fieldset('', 'name', 'surname', 'status', 'salary', 'specialty', 'grage',
                     'education', 'experience', 'portfolio'), Submit('submit', 'Сохранить',
                                                                     css_class='btn btn-info')))

    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grage',
                  'education', 'experience', 'portfolio']
        labels = {'name': 'Имя', 'surname': 'Фамилия', 'status': 'Готовность к работе', 'salary':
                  'Ожидаемое вознаграждение', 'specialty': 'Специализация', 'grage': 'Квалификация',
                  'education': 'Образование', 'experience': 'Опыт работы',
                  'portfolio': 'Ссылка на портфолио'}
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'type': "text",
                                           'id': "userName"}),
            'surname': forms.TextInput(attrs={'class': "form-control", 'type': "text",
                                              'id': "userSurname"}),
            'status': forms.Select(attrs={'class': "custom-select mr-sm-2", 'id': "userReady"}),

            'salary': forms.NumberInput(attrs={'class': "form-control", 'type': "text",
                                               'id': "userPortfolio"}),
            'specialty': forms.Select(attrs={'class': "custom-select mr-sm-2",
                                             'id': "userSpecialization"}),
            'grage': forms.Select(attrs={'class': "custom-select mr-sm-2",
                                         'id': "userQualification"}),
            'education': forms.Textarea(attrs={'class': "form-control text-uppercase", 'rows': "4",
                                               'id': "userEducation", 'style': "color:#000;"}),
            'experience': forms.Textarea(attrs={'class': "form-control", 'rows': "4",
                                                'id': "userExperience", 'style': "color:#000;"}),
            'portfolio': forms.TextInput(attrs={'class': "form-control", 'type': "text",
                                                'placeholder': "http://anylink.github.io",
                                                'id': "userPortfolio"})


        }

