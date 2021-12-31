from BeautifulSoup4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data = requests.get(url)
html_data = html_data.content

soup = BeautifulSoup(html_data, "html.parser")

data = pd.DataFrame(columns=["Rank","Name","Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    if col != []:
        rank = col[0].text.replace('\n','')
        name = col[1].text.replace('\n','')
        mony = col[2].text.replace('\n','')
        data = data.append({"Rank":rank,"Name":name, "Market Cap (US$ Billion)":mony}, ignore_index=True)

data = data.to_json(r'bank_market_cap.json')