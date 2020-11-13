from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    description = models.TextField()
    employee_count = models.IntegerField()
    logo = models.CharField(max_length=120)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=500)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()


