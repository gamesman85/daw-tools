#!python3

import re
from btc import *
from timephrase import *
import time

# Wait until the next minute starts
sleeptime = 60 - datetime.utcnow().second
time.sleep(sleeptime)

# Find the date of execution
present = datetime.now()
dateString = ("Date: " + present.strftime('%d %B'))

# Open file to keep track of price changes
f = open('prices.txt', 'w')

f.write(dateString + '\n')

print(dateString)

# Log the bitcoin price for every minute of the upcoming hour
for i in range(60):
  present = datetime.now()
  timeString = present.strftime('%H:%M')
  btc_price = btc()

  f.write(timeString + ' ' + btc_price + '\n')
  
  print(timeString, btc_price)
  time.sleep(60)

f.close()

# Processing the information so it can be presented in a CSV file.
price_regex = re.compile(r'\d{2},\d{3}\.\d{2}')

f = open('prices.txt', 'r')

match = price_regex.findall(f.read())

f.close()

f = open('prices.csv', 'w')

f.write('Time,Price\n')

 # Represent every minute with numbers starting from 1, remove unnecessary commas from price.
for i in range(len(match)):
  f.write(str(i+1) + ',' + str(match[i]).replace(',','') + '\n')

f.close()