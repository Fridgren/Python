import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import tabulate

# raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, 2, 3],
# 'postTestScore': [25, 94, 57, 62, 70]}

# Create a dataframe
# raw_df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])




# Create a variable with the URL to this tutorial
url = 'https://recruit.visma.com/External/OJCustomer3/AssignmentList.aspx?guidExtSoftware=9659fe31-b94b-424c-88c1-d502044c8fee'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, "html5lib")

Befattning = []
Avdelning = []
Sök_senast = []  # preTestScore = []
# postTestScore = []


# Create an object of the first object that is class=dataframe
table = soup.find('table')
#print(table)

# # Find all the <tr> tag pairs, skip the first one, then for each.
for row in table.find_all('tr')[1:]:
    #     # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')
    #
    #     # Create a variable of the string inside 1st <td> tag pair,
    column_1 = col[0].string.strip()
#     # and append it to first_name variable
    Befattning.append(column_1)
#
#     # Create a variable of the string inside 2nd <td> tag pair,
    column_2 = col[1].string.strip()
#     # and append it to last_name variable
    Avdelning.append(column_2)
#
#     # Create a variable of the string inside 3rd <td> tag pair,
    column_3 = col[2].string.strip()
#     # and append it to age variable
    Sök_senast.append(column_3)  #
#     # Create a variable of the string inside 4th <td> tag pair,
#     column_4 = col[3].string.strip()
#     # and append it to preTestScore variable
#     preTestScore.append(column_4)
#
#     # Create a variable of the string inside 5th <td> tag pair,
#     column_5 = col[4].string.strip()
#     # and append it to postTestScore variable
#     postTestScore.append(column_5)
#
# # Create a variable of the value of the columns
columns = {'Befattning': Befattning, 'Avdelning': Avdelning,
           'Sök_senast':Sök_senast}  # , 'preTestScore': preTestScore, 'postTestScore': postTestScore}
#
# # Create a dataframe from the columns variable
df = pd.DataFrame(columns)
#
print(df)




