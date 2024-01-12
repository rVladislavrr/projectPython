import sqlite3
def run():
    conn = sqlite3.connect('db.sqlite3')
    conn.execute('delete from SalaryOnyear')
    conn.execute("DELETE FROM sqlite_sequence WHERE name= 'SalaryOnYear'")
    conn.execute("""insert into SalaryOnYear (year, salary_avg)
                    select substr(published_at,1,4),round(avg(salary_avg),2)
                    from salary_vac
                    where salary_avg between 12000 and 1000000 group by  substr(published_at,1,4)
                    """)
    conn.commit()