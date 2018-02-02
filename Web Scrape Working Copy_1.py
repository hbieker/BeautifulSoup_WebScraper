import requests
import csv
from bs4 import BeautifulSoup

#Get page 
page = requests.get('https://coinmarketcap.com/currencies/ethereum/historical-data/')

#Create BeautifluSoup object. Case-sensitive!
soup = BeautifulSoup(page.text, 'html.parser')

#Find all td tags. Stores each table data in a list (array)
price_list_items = soup.findAll('td')

#Create new CSV file and write column headers
file = csv.writer(open('Monthly-Ethereum-Prices.csv', 'w', newline=''))
file.writerow(['MONTHLY ETHEREUM MARKET DATA'])
file.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap'])

#Get the Ethereum data contents from the <td> tags and move them into a list
all_stats_list = []
for price_only in price_list_items:
    price = price_only.contents[0]
    all_stats_list.append(price)

#Loop through 7 elements at a time and write the list to file
while all_stats_list:
    one_line_of_stats = []
    for stats in all_stats_list[0:7]:
        stat = all_stats_list[0]
        one_line_of_stats.append(stat)
        all_stats_list.pop(0)
    file.writerow(one_line_of_stats)
