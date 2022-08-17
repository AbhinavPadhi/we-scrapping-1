from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url)
print(page)
soup = bs(page.text,'html.parser')
star_table = soup.find('table')
temporary= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temporary.append(row)

StarName = []
Distance =[]
Mass = []
Radius =[]
Luminosity = []

for a in range(1,len(temporary)):
    StarName.append(temporary[a][1])
    Distance.append(temporary[a][3])
    Mass.append(temporary[a][5])
    Radius.append(temporary[a][6])
    Luminosity.append(temporary[a][7])
    
data = pd.DataFrame(list(zip(StarName,Distance,Mass,Radius,Luminosity)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

data.to_csv('project.csv')