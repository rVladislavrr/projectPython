# Create your views here.
import threading

from django.shortcuts import render
import requests
from .models import OnYear, Skills_MyVac, Skills_Vac_Full,City
from datetime import datetime
from bs4 import BeautifulSoup

cxt_new_vac = {
    'err': 'Загружается, обновите страницу',
}


def reqvest():

    def fetch_vacancies():
        keywords = ['fullstack', 'фулстак', 'фуллтак', 'фуллстэк', 'фулстэк', 'full stack']
        today = datetime.now().replace(hour=0, minute=0, second=0)
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": " OR ".join(keywords),
            "date_from": today.isoformat(),
            "per_page": 10,
            "order_by": "publication_time"
        }
        response = requests.get(url, params=params)
        data = response.json()
        vacancies = data.get("items", [])
        result = []

        for vacancy in vacancies:
            vacancy_data = {
                "name": vacancy["name"],
                "employer_name": vacancy["employer"]["name"],
                "salary": vacancy.get("salary", ""),
                "area_name": vacancy["area"]["name"],
                "published_at": vacancy["published_at"].replace('T', ' ')[:19] + ' (по Мск)',
                'url': f"https://hh.ru/vacancy/{vacancy["id"]}"
            }

            description, skills = get_vacancy_details(vacancy["id"])
            description_sh = description[: description.find(';' , description.find(';') + 1 )] + '...'
            description_ds = description[: description.find('.' , description.find('.') + 1 )] + '...'

            vacancy_data["description"] = description_sh if len(description_sh) < len(description_ds) else description_ds
            vacancy_data["skills"] = skills

            result.append(vacancy_data)

        return result

    def get_vacancy_details(vacancy_id):
        url = f"https://api.hh.ru/vacancies/{vacancy_id}"
        response = requests.get(url)
        data = response.json()

        description = data.get("description", "")

        skills = ""
        if "key_skills" in data and data["key_skills"]:
            skills = ", ".join([skill["name"] for skill in data["key_skills"]])

        return remove_html_tags(description), skills

    def remove_html_tags(text):
        soup = BeautifulSoup(text, "html.parser")
        cleaned_text = soup.get_text()
        return cleaned_text

    vacancies = fetch_vacancies()
    dict_ = {'vac': vacancies}
    global cxt_new_vac
    cxt_new_vac = dict_


def year_salar():
    dict_ = {}
    items = OnYear.objects.all()
    for i in range(len(items)):
        items[i].salary_avg = round(items[i].salary_avg, 2)
        items[i].salary_avg_for_vac = round(items[i].salary_avg_for_vac, 2)
    dict_['items'] = items
    return dict_

def City_year():
    dict_ = {}
    items = City.objects.all()
    for i in range(len(items)):
        items[i].salary_vac = round(items[i].salary_vac, 2)
        items[i].count = round(items[i].count, 3)
        items[i].salary = round(items[i].salary, 2)
        items[i].count_vac = round(items[i].count_vac, 3)

    dict_['items_salar'] = items
    dict_['items_count'] = sorted(items, key = lambda x: x.count,reverse=True)
    dict_['items_salary_vac'] = sorted(items, key = lambda x: x.salary_vac,reverse=True)
    dict_['items_count_vac'] = sorted(items, key = lambda x: x.count_vac,reverse=True)
    return dict_


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


def index_page(request):
    t1 = threading.Thread(target=reqvest)
    t1.start()
    return render(request, 'main.html')


def page_2(request):
    dict_ = year_salar()
    return render(request, 'vostr.html', context=dict_)


def page_3(request):
    dict_ = City_year()
    return render(request, 'geo.html', context=dict_)


def page_4(request):
    dict_ = {'items': render_for_vac()}
    return render(request, 'skills.html', context=dict_)


def page_5(request):
    t1 = threading.Thread(target=reqvest)
    t1.start()
    global cxt_new_vac
    return render(request, 'new_vac.html', context=cxt_new_vac)
