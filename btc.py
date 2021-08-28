#!python3

import requests, bs4

def btc():
  res = requests.get('https://coinmarketcap.com')
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select('td div')
  price = elems[8].getText()
  return price