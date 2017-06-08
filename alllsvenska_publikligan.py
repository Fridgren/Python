import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib

url = 'https://www.allsvenskan.se/tabell'

r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

lag = []
hemmasnitt = []
hemmatotal = []
bortasnitt = []
bortatotal = []
totalsnitt = []
totalt = []



table = soup.find(class_='attendance-widget')
#print(table)


for row in table.find_all('tr')[1:-1]:

    col = row.find_all('td')

    column_1 = col[0].string.strip()
    lag.append(column_1)


    column_2 = col[1].string.strip()
    hemmasnitt.append(column_2)

    column_3 = col[2].string.strip()
    hemmatotal.append(column_3)

    column_4 = col[3].string.strip()
    bortasnitt.append(column_4)

    column_5 = col[4].string.strip()
    bortatotal.append(column_5)

    column_6 = col[5].string.strip()
    totalsnitt.append(column_6)

    column_7 = col[6].string.strip()
    totalt.append(column_7)

columns = {'lag': lag,
           'hemmasnitt': hemmasnitt,
           'hemmatotal': hemmatotal,
           'bortasnitt': bortasnitt,
           'bortatotal': bortatotal,
           'totalsnitt': totalsnitt,
           'totalt': totalt}


df = pd.DataFrame(columns)

print(df)
