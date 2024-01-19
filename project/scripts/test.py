from project.models import OnYear, City
import matplotlib.pyplot as plt
import numpy as np

def run():
    def plot_year():
        items = OnYear.objects.all()
        x = []
        y = []
        for i in items:
            x.append(i.year)
            y.append(i.salary_avg)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Год')
        ax.set_ylabel('Зарплата')
        ax.set_title('Динамика зарплат по годам')
        plt.xticks(rotation=45)
        fig.set_size_inches(8, 6)
        plt.savefig('static/img/Salar_year1.png')

    def plot_year_c():
        items = OnYear.objects.all()
        x = []
        y = []
        for i in items:
            x.append(i.year)
            y.append(i.count)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Год')
        ax.set_ylabel('Кол-во вакансий')
        ax.set_title('Динамика вакансий по годам')
        plt.xticks(rotation=45)
        fig.set_size_inches(8, 6)
        plt.savefig('static/img/Count_year.png')

    def plot_year_salary_vac():
        items = OnYear.objects.all()
        x = []
        y = []
        for i in items:
            x.append(i.year)
            y.append(i.salary_avg_for_vac)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Год')
        ax.set_ylabel('Средняя зп')
        ax.set_title('Динамика зарплат Fullstack раз.')
        plt.xticks(rotation=45)
        fig.set_size_inches(8, 6)
        plt.savefig('static/img/Salary_vac_year1.png')

    def plot_year_count_vac():
        items = OnYear.objects.all()
        x = []
        y = []
        for i in items:
            x.append(i.year)
            y.append(i.count_vac)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Год')
        ax.set_ylabel('Кол-во вакансий')
        ax.set_title('Динамика вакансий Fullstack раз.')
        plt.xticks(rotation=45)
        fig.set_size_inches(8, 6)
        plt.savefig('static/img/Count_vac_year.png')

    # plot_year_c()
    # plot_year()
    # plot_year_salary_vac()
    # plot_year_count_vac()

    items = City.objects.all()
    cities = []
    average_salaries = []


    for i in items:
        cities.append(i.city)
        average_salaries.append(i.salary_vac)
    sorted_data = sorted(zip(cities, average_salaries), key=lambda x: x[1], reverse=False)
    sorted_cities = [item[0] for item in sorted_data]
    sorted_salaries = [item[1] for item in sorted_data]

    plt.figure(figsize=(8, 6))  # Устанавливаем размер диаграммы
    bars = plt.barh(sorted_cities, sorted_salaries)  # Используем plt.barh для горизонтальной диаграммы

    # Добавляем названия городов справа
    plt.yticks(fontsize=12)  # Устанавливаем размер шрифта для названий городов

    # Добавляем подписи осей и заголовок
    plt.xlabel('Средняя зарплата')
    plt.title('Средняя зарплата по городам ')
    plt.yticks(fontsize=6)
    plt.xticks(fontsize=8)
    # Отображаем диаграмму

    plt.savefig('static/img/Salary_city.png')


    # Рисуем круговую диаграмму
    # plt.figure(figsize=(8, 6))
    # plt.pie(average_salaries, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 7})
    # plt.axis('equal')
    #
    #
    # plt.legend(loc='lower left',labels = cities, fontsize='x-small')
    # plt.title('Доля вакансий по городам для Fullstack')
    #
    # plt.savefig('static/img/Count_city_vac.png')

