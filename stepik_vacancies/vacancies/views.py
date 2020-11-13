from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Specialty


class MainView(TemplateView):
    template_name = 'vacancies/index.html'


class AllVacanciesView(ListView):
    template_name = 'vacancies/vacancies.html'


class SpecialVacanciesView(ListView):
    template_name = 'vacancies/vacancies.html'


class CompanyView(DetailView):
    template_name = 'vacancies/company.html'


class VacancyView(DetailView):
    template_name = 'vacancies/vacancy.html'

