import requests
from bs4 import BeautifulSoup

url = 'https://url.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    for titles in source.find_all('title'):
        print(titles.get_text())
