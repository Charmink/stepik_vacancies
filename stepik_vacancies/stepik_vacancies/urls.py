"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vacancies.views import MainView, AllVacanciesView, SpecialVacanciesView, CompanyView, \
    VacancyView, SendView, MyCompanyView, MyLoginView, MySignupView, MyVacanciesView, MyVacancyView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:specialty>/', SpecialVacanciesView.as_view(),
         name='special_vacancies'),
    path('vacancies/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('companies/<int:pk>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:pk>/send/', SendView.as_view(), name='send_vacancy'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:pk>/', MyVacancyView.as_view(), name='my_vacancy'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
