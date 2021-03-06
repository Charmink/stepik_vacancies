# Generated by Django 3.1.3 on 2020-12-07 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0004_auto_20201207_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('Не ищу работу', 'Не ищу работу'), ('Рассматриваю предложения', 'Рассматриваю предложения'), ('Ищу работу', 'Ищу работу')], default='Ищу работу', max_length=64)),
                ('salary', models.IntegerField()),
                ('grage', models.CharField(choices=[('Стажер', 'Стажер'), ('Джуниор', 'Джуниор'), ('Миддл', 'Миддл'), ('Синьор', 'Синьор'), ('Лид', 'Лид')], default='Стажер', max_length=64)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.TextField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='vacancies.specialty')),
            ],
        ),
    ]
