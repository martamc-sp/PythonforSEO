import requests
from bs4 import BeautifulSoup

url = 'https://upzerk.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    count += 1
    response = requests.get(websiteurls)
    print(websiteurls)
    print(response)
    print(count)
