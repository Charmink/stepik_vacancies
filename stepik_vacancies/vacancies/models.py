from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    description = models.TextField()
    employee_count = models.IntegerField()
    logo = models.ImageField(upload_to='company_logos', height_field='height_field',
                             width_field='width_field')
    height_field = models.PositiveIntegerField(default=150)
    width_field = models.PositiveIntegerField(default=150)
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE,
                              default=User.objects.use_in_migrations)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='specialty_pictures', height_field='height_field',
                                width_field='width_field')
    height_field = models.PositiveIntegerField(default=150)
    width_field = models.PositiveIntegerField(default=150)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()


class Application(models.Model):
    written_username = models.CharField(max_length=128)
    written_phone = models.CharField(max_length=15)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
