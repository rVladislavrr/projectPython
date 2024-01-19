import time
import pandas as pd
from datetime import datetime
from dateutil import rrule
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.filterwarnings('ignore', message="DateTimeField Valute.date received a naive datetime", category=RuntimeWarning)

def main(main_df):
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=datetime(2003, 1, 1), until=datetime(2023, 12, 1)):
        URL = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{dt.strftime("%m/%Y")}'
        df = pd.read_xml(URL, encoding='ISO-8859-1')
        df['date'] = dt.strftime("%Y-%m")
        df['Value'] = df['Value'].str.replace(',', '.')
        df['VunitRate'] = (df['Value'].astype(float) / df['Nominal'].astype(int)).round(8)
        df = df.pivot(index='date', columns='CharCode', values='VunitRate').reset_index()
        main_df = main_df._append(df, ignore_index=True, sort=False)
    return main_df

def run():
    t = time.time()
    columns_ = ['date', 'BYR', 'USD', 'EUR', 'KZT', 'UAH', 'AZN', 'KGS', 'UZS', 'GEL']
    main_df = pd.DataFrame(columns=columns_)
    main_df = main(main_df)
    main_df = main_df[columns_]
    main_df.to_csv('csv/currency.csv', index=False)
    print(time.time()-t)