# Create your views here.
from django.shortcuts import render
import requests
from datetime import datetime
from bs4 import BeautifulSoup


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
                "published_at": vacancy["published_at"]
            }

            description, skills = get_vacancy_details(vacancy["id"])
            vacancy_data["description"] = description
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
    return dict_


def index_page(request):
    ctx = reqvest()
    return render(request, 'home_page.html', context=ctx)
