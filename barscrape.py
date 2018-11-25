from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.timeout.com/london/bars-pubs'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
bars = soup.find("div")
bar_names=bars.find_all("h3")

#Creating a loop to get clean data without special characters or html tags. Assigning the clean names to a list called 'bar_list'.

bar_list = []
for b in bar_names[0:]:
    result = b.text.strip()
    bar_list.append(result)


print(bar_list)
bar_list = bar_list[:-9]
print(bar_list)
len(bar_list)
bar_address = bars.find_all("em")


address_list = []
for a in bar_address[0:]:
    result2 = a.text.strip()
    address_list.append(result2)


print(address_list)


address_list = address_list[:-1]

print(address_list)

len(address_list)

minn_bars = pd.DataFrame({'Bars': bar_list,'Address & Contact': address_list})

print(minn_bars)


