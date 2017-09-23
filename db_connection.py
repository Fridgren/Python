

import pymysql


conn = pymysql.connect(host='mysql.dsv.su.se', port=3306, user='cefr7413', passwd='iew9ohXaiRah', db='cefr7413')

cur = conn.cursor()


cur.execute("SELECT userid, mail, regdate FROM user")

print(cur.description)

print()

for row in cur:
    print(row)


cur.close()
conn.close()


