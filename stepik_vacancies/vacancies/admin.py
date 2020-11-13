from django.contrib import admin
from .models import Company, Specialty, Vacancy

admin.site.register(Vacancy)
admin.site.register(Specialty)
admin.site.register(Company)
