

import pymysql


conn = pymysql.connect(host='xxxxx', port=3306, user='xxxxx', passwd='xxxx', db='xxxx')

cur = conn.cursor()

cur.execute("SELECT * FROM user")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()


