from django.views.generic import ListView, DetailView, TemplateView
from .models import Specialty, Company, Vacancy, Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ApplicationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from .forms import MyUserCreationForm, ApplicationForm
from django.urls import resolve


class MainView(ListView):
    template_name = 'vacancies/index.html'
    model = Specialty

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        print(context['object_list'][1].vacancies.all())
        return context


class AllVacanciesView(ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancy


class SpecialVacanciesView(ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancy

    def get_queryset(self):
        specialty = self.kwargs.get('specialty', None)
        queryset = Vacancy.objects.filter(specialty=Specialty.objects.get(code=specialty))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SpecialVacanciesView, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.filter(code=self.kwargs.get('specialty', None))[0].title
        print(context)
        return context


class CompanyView(DetailView):
    template_name = 'vacancies/company.html'
    model = Company


class VacancyView(CreateView):
    template_name = 'vacancies/vacancy.html'
    model = Application
    form_class = ApplicationForm

    def form_valid(self, form):
        application = form.save(commit=False)
        application.user = self.request.user
        application.vacancy = Vacancy.objects.get(id=self.request.resolver_match.kwargs.get('pk', None))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)
        context['object'] = Vacancy.objects.get(id=int(self.kwargs.get('pk', None)))
        print(context)
        return context

    def get_success_url(self):

        return reverse_lazy('send_vacancy', kwargs={'pk': self.request.resolver_match.kwargs.get('pk')})


class MySignupView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'vacancies/register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'vacancies/login.html'


class SendView(TemplateView):
    template_name = 'vacancies/sent.html'


class MyCompanyView(DetailView):
    pass


class MyVacanciesView(ListView):
    pass


class MyVacancyView(DetailView):
    pass
