import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_vacancies.settings')
django.setup()

from .vacancies.models import Specialty
from data import specialties

for specialty in specialties:
    Specialty.objects.create(title=specialty['title'], picture=specialty['picture'],
                             code=specialty['code'])
