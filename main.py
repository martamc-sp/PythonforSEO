import requests
from bs4 import BeautifulSoup

""" Everything we do is available in this file. But if you want to view it individually, visit the Lessons file. """

url = 'https://upzerk.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    count += 1
    print(websiteurls)
    print(count)