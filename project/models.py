from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.TextField(null=True, default=None)
    key_skills = models.TextField(null=True, default=None)
    salary_from = models.IntegerField(null=True, default=None)
    salary_to = models.IntegerField(null=True, default=None)
    salary_currency = models.CharField(max_length=3, null=True, default=None)
    area_name = models.TextField(null=True, default=None)
    published_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return f"{self.name} {self.area_name} {self.published_at}"

    class Meta:
        db_table = 'vacancy'
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
        ]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    pass


class Salary_vac(models.Model):
    name = models.TextField(null=True, default=None)
    salary_avg = models.FloatField(null=True)
    area_name = models.TextField(null=True, default=None)
    published_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return f'{self.name} {self.salary_avg} {self.area_name} {self.published_at}'

    class Meta:
        db_table = 'salary_vac'
        verbose_name = "avg_salary"
        verbose_name_plural = "avg_salary"

    pass


class OnYear(models.Model):
    year = models.CharField(max_length=5, null=True)
    salary_avg = models.FloatField(null=True)
    salary_avg_for_vac = models.FloatField(null=True,blank=True)
    count = models.IntegerField(null=True)
    count_vac = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'Год: {self.year} и статистика {self.salary_avg, self.salary_avg_for_vac, self.count, self.count_vac}'

    class Meta:
        db_table = 'Year'
        verbose_name = "year"
        verbose_name_plural = "year"


# class Filter_Vac(models.Model):
#     name = models.TextField(null=True, default=None)
#     key_skills = models.TextField(null=True, default=None)
#     salary_from = models.IntegerField(null=True, default=None)
#     salary_to = models.IntegerField(null=True, default=None)
#     salary_currency = models.CharField(max_length=3, null=True, default=None)
#     area_name = models.TextField(null=True, default=None)
#     published_at = models.DateTimeField(null=True, default=None)
#
#     def __str__(self):
#         return f"фулл стек {self.area_name}  {self.published_at}"
#
#     class Meta:
#         db_table = 'Filter_Vac'
#         verbose_name = "Filter_Vac"
#         verbose_name_plural = "Filter_Vac"
#
#     pass


class City(models.Model):
    city = models.TextField(null=True)
    salary = models.FloatField(null=True)
    count = models.FloatField(null=True)
    salary_vac = models.FloatField(null=True,blank=True)
    count_vac = models.FloatField(null=True,blank=True)

    def __str__(self):
        return f'Город: {self.city} статистика: {self.salary, self.salary_vac, self.count_vac, self.count_vac}'

    class Meta:
        db_table = 'City'
        verbose_name = "City"
        verbose_name_plural = "City"