import sqlite3
import time
import csv
def run():
    add()
def add():
    connection = sqlite3.connect('db.sqlite3')
    time_start = time.time()
    with open('vacancies.csv', encoding='utf-8-sig') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        i = 0
        next(file_reader)
        for row in file_reader:
            connection.execute('''insert into vacancy
            (name,key_skills,salary_from,salary_to,salary_currency,area_name,published_at) 
            values(?,?,?,?,?,?,?)''', row)
            i+=1
            if i % 1000000 == 0:
                print(time.time() - time_start, i)
                connection.commit()

    connection.commit()
    connection.close()
    print("last: ", time.time()-time_start, i)


