#!python3

import requests, bs4, os
from download import *

dl_from = input('Download images from: ')
res = requests.get(dl_from)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
site_images = soup.select('img')
for image in site_images:
  image_src = image.get('src')
  dl_url = os.path.dirname(dl_from) + '/' + os.path.basename(image_src)
  download(dl_url, image_src, False)