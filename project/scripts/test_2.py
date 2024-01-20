from project.models import Skills_MyVac,Skills_Vac_Full

def render_for_vac():
    result = []

    skills_Full = Skills_Vac_Full.objects.all()

    year_data = {}

    for skill in skills_Full:
        year = skill.year
        skill_name = skill.skill
        quantity = skill.count

        if year not in year_data:
            year_data[year] = []

        year_data[year].append({'name': skill_name, 'count': quantity})

    year_data_vac = {}
    skills = Skills_MyVac.objects.all()
    for skill in skills:
        year = skill.year
        skill_name = skill.skill
        quantity = skill.count

        if year not in year_data_vac:
            year_data_vac[year] = []

        year_data_vac[year].append({'name': skill_name, 'count': quantity})

    for year, skills, in year_data.items():
        skills_f = year_data_vac[year]
        result.append({'year': year, 'skills_full': skills,'skills_vac': skills_f})
    return result
def run():
    res = render_for_vac()
    for i in res:
        print(i['year'])
        print('/////////////////')
        for j in i['skills_full']:
            print(j['name'])
        print('/////////////////')
        for j in i['skills_vac']:
            print(j['name'])
        print('/////////////////')