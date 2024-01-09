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


class Valute(models.Model):
    date = models.DateTimeField(null=False, default=None)
    BYR = models.FloatField(null=True)
    USD = models.FloatField(null=True)
    EUR = models.FloatField(null=True)
    KZT = models.FloatField(null=True)
    UAH = models.FloatField(null=True)
    AZN = models.FloatField(null=True)
    KGS = models.FloatField(null=True)
    UZS = models.FloatField(null=True)
    GEL = models.FloatField(null=True)

    def __str__(self):
        return f'{self.date} в эту дату значения есть'

    class Meta:
        db_table = 'valute'
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    pass
