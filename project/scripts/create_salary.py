import pandas as pd
from threading import Thread
from django.db import connections, transaction
import warnings
import time

warnings.simplefilter(action='ignore')

def run():
    thread = Thread(target=process_vacancies)
    thread.start()

def convert_currency(vacancy_row, exchange_rates):
    if vacancy_row["salary_currency"] != "RUR" and not pd.isna(vacancy_row["salary"]):
        published_at = vacancy_row["published_at"].normalize().replace(day=1).tz_localize(None)
        rate = exchange_rates.loc[published_at, vacancy_row["salary_currency"]]
        vacancy_row["salary"] = int(rate * vacancy_row["salary"]) if not pd.isna(rate) else None
    return vacancy_row

def format_published_date(date):
    formatted_date = date.strftime("%Y-%m-%dT%T%z")
    return formatted_date

def convert_and_format_data(vacancies_data, exchange_rates):
    exchange_rates.index = pd.to_datetime(exchange_rates.index)
    vacancies_data['published_at'] = pd.to_datetime(vacancies_data['published_at'])

    vacancies_data = vacancies_data.dropna(subset=["salary_from", "salary_to"], how="all")

    vacancies_data["salary"] = vacancies_data[["salary_from", "salary_to"]].mean(axis=1)
    vacancies_data = vacancies_data.apply(convert_currency, axis=1, exchange_rates=exchange_rates)
    vacancies_data["published_at"] = vacancies_data["published_at"].apply(format_published_date)
    vacancies_data = vacancies_data[["name", "salary", "area_name", "published_at"]]
    return vacancies_data

def process_vacancies():
    df_currency = pd.read_csv('csv/currency.csv', index_col='date')
    csv_merged = pd.read_csv('csv/vacancies.csv')

    vacancies_data = convert_and_format_data(csv_merged, df_currency)
    t = time.time()
    # Сохранение данных в базу данных
    with connections['default'].cursor() as cursor:
        with transaction.atomic():
            for index, row in vacancies_data.iterrows():
                print(time.time()-t, index)
                cursor.execute(
                """
                INSERT INTO salary_vac (name, salary_avg, area_name, published_at)
                VALUES (%s, %s, %s, %s)
                """,
                [row['name'], row['salary'], row['area_name'], row['published_at']]
                )

