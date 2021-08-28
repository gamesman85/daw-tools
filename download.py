#!python3

import requests

def download(source, target):
  print('Downloading ' + source + ' to ' + target + '...')
  res = requests.get(source)
  f = open(target, 'wb')
  for chunk in res.iter_content(100000):
    f.write(chunk)
  f.close()
  print('Download finished.')