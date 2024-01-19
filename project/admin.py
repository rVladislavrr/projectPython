from django.contrib import admin

# Register your models here.
from project.models import *

admin.site.register(Vacancy)
admin.site.register(Salary_vac)
admin.site.register(OnYear)
admin.site.register(City)
admin.site.register(Skills_MyVac)
admin.site.register(Skills_Vac_Full)

