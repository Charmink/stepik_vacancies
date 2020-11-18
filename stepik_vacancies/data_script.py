import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_vacancies.settings')
django.setup()

from vacancies.models import Vacancy, Specialty, Company
from data import specialties, jobs
from datetime import date

for specialty in Specialty.objects.all():
    print(specialty.picture)
