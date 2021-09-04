import requests
from bs4 import BeautifulSoup
import json

url = 'https://upzerk.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    imagesfinder = source.find_all('img')
    imagelist = []
    print(websiteurls)
    for images in imagesfinder:        
        try:     
            foundedimages = images['alt']
        except:
            foundedimages = 'We dont have image'
        images = foundedimages
        imagelist.append(images)
    print(json.dumps(imagelist))