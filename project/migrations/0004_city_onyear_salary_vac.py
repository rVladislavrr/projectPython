# Generated by Django 5.0 on 2024-01-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_vacancy_area_name_alter_vacancy_key_skills_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(null=True)),
                ('salary', models.FloatField(null=True)),
                ('count', models.FloatField(null=True)),
                ('salary_vac', models.FloatField(blank=True, null=True)),
                ('count_vac', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='OnYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, null=True)),
                ('salary_avg', models.FloatField(null=True)),
                ('salary_avg_for_vac', models.FloatField(blank=True, null=True)),
                ('count', models.IntegerField(null=True)),
                ('count_vac', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'year',
                'verbose_name_plural': 'year',
                'db_table': 'Year',
            },
        ),
        migrations.CreateModel(
            name='Salary_vac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None, null=True)),
                ('salary_avg', models.FloatField(null=True)),
                ('area_name', models.TextField(default=None, null=True)),
                ('published_at', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'avg_salary',
                'verbose_name_plural': 'avg_salary',
                'db_table': 'salary_vac',
            },
        ),
    ]
