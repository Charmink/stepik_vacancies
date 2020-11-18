from django.views.generic import ListView, DetailView
from .models import Specialty, Company, Vacancy


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


class VacancyView(DetailView):
    template_name = 'vacancies/vacancy.html'
    model = Vacancy
