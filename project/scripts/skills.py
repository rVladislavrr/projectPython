import csv
from collections import Counter
import time

import sqlite3

def run():
    conn = sqlite3.connect('db.sqlite3')
    t = time.time()
    skills_by_year = {}

    with open('csv/vacancies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)


        for row in reader:
            year = row['published_at'][:4]
            skills = row['key_skills'].split('\n')


            skills = [skill.strip() for skill in skills if skill.strip()]

            if year in skills_by_year:
                skills_by_year[year].extend(skills)
            else:
                skills_by_year[year] = skills
    for year, skills in skills_by_year.items():
        skills_count = Counter(skills)
        for skill, count in skills_count.most_common(20):
            conn.execute(f"insert into skills_Full(year, skill, count)  values ({year},'{skill}',{count})")
    print('///////////////////////')



    skills_by_year = {}


    with open('csv/vacancies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)


        for row in reader:
            year = row['published_at'][:4]
            skills = row['key_skills'].split('\n')
            name = row['name']

            skills = [skill.strip() for skill in skills if skill.strip()]


            if any(word in name.lower() for word in
                   ['fullstack', 'фулстак', 'фуллтак', 'фуллстэк', 'фулстэк', 'full stack']):

                if year in skills_by_year:
                    skills_by_year[year].extend(skills)
                else:
                    skills_by_year[year] = skills
    for year, skills in skills_by_year.items():
        skills_count = Counter(skills)
        for skill, count in skills_count.most_common(20):
            conn.execute(f"insert into MyVac_skills(year, skill, count)  values ({year}, '{skill}', {count})")
    conn.commit()
    print(time.time()-t)