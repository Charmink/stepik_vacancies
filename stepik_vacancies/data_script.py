import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_vacancies.settings')
django.setup()

from vacancies.models import Vacancy, Specialty, Company
from data import specialties, jobs, companies
from datetime import date

for vacancy in jobs:
    date_ = [int(i) for i in vacancy['posted'].split('-')]
    for company in companies:
        if company['id'] == vacancy['company']:
            name = company['title'].capitalize()
    Vacancy.objects.create(title=vacancy['title'], specialty=Specialty.objects.get(code=vacancy['specialty']),
                           company=Company.objects.get(name=name), salary_min=int(vacancy['salary_from']),
                           salary_max=int(vacancy['salary_to']), skills=vacancy['skills'],
                           description=vacancy['description'], published_at=date(date_[0], date_[1], date_[2])
                           )
