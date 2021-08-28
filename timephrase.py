#!python3

from datetime import time, datetime

def timephrase():
  present = datetime.now()
  phrase = present.strftime('%A %d %B %Y, %H:%M')
  return phrase