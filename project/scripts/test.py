from project.models import OnYear
import matplotlib.pyplot as plt


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
    plot_year_salary_vac()
    plot_year_count_vac()
