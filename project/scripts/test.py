from project.models import *
def run():
    vac = Count_VacOnYear.objects.all()
    print(*vac)