

import pymysql


conn = pymysql.connect(host='###', port='###', user='###', passwd='###', db='###')

cur = conn.cursor()


cur.execute("SELECT userid, mail, regdate FROM user")

print(cur.description)

print()

for row in cur:
    print(row)


cur.close()
conn.close()


