import pymysql
import sys

print(sys.stdin.encoding)

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='wpfkem19',
                                 db='tradinginfo', charset ='utf8')
cur = conn.cursor()
cur.execute("SELECT * FROM tob_code")

print("초기 db ")
for row in cur:
   print(row[0])

#sql = "insert into tod_code ( code, name ) values (444, '키움증권')"
sql = "INSERT INTO tob_code (code, name) VALUES (555, '키움증권')"

cur.execute(sql)
conn.commit()

cur.execute("SELECT * FROM tob_code")

print("삽입 후 db ")
for row in cur:
   print(row[0])


cur.close()
conn.close()