#!python3

import requests
from speak import *

def download(source, target, sound):
  txt = 'Downloading ' + source + ' to ' + target + '...'
  print(txt)
  if sound:
    speak(txt)
  
  res = requests.get(source)
  res.raise_for_status()
  f = open(target, 'wb')
  for chunk in res.iter_content(100000):
    f.write(chunk)
  f.close()
  
  txt = 'Download finished.'
  print(txt)
  if sound:
    speak(txt)