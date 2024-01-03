from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.TextField()
    key_skills = models.TextField()
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    salary_currency = models.CharField(max_length=3)
    area_name = models.TextField()
    published_at = models.DateTimeField()

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
