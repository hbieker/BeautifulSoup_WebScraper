import requests
import csv
from bs4 import BeautifulSoup

#Get page and verify 200 status code for response
page = requests.get('https://coinmarketcap.com/currencies/ethereum/historical-data/')
print(page.status_code)

#Create BeautifluSoup object. Case-sensitive!
soup = BeautifulSoup(page.text, 'html.parser')

#Find all td tags. Stores each table data in a list (array)
#price_list = soup.find('tbody')
price_list_items = soup.findAll('td')

#remove_html = soup.find(class_='col-xs-12 col-md-6 text-right')
#remove_html.decompose()

#remove_menu = soup.find(class_='dropdown-menu')
#remove_menu.decompose()

#Print Ethereum Prices - includes all html tags
#for price in price_list_items:        
#    print (price)

#for price_only in price_list_items:
#    price = price_only.contents[0]
#    print (price)

#Create new CSV file and write column headers
file = csv.writer(open('Monthly-Ethereum-Prices.csv', 'w'))
file.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap'])

#Print Ethererum Prices - data only w/no tags!
day1 = []
for price_only in price_list_items[0:7]:
    price = price_only.contents[0]
    day1.append(price)
    print (day1)
file.writerow(day1)
    
    
