import pandas as pd
from collections import Counter




def run():
    vacancies = pd.read_csv('csv/vacancies.csv')
    skills = vacancies['key_skills'].dropna(axis=0).apply(lambda x: x.split('\r\n')).tolist()
    res = sorted(dict(Counter(sum(skills, []))).items(), key=lambda item: item[1], reverse=True)
    print(res[:14])

