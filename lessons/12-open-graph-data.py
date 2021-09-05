import requests
from bs4 import BeautifulSoup

""" Youtube : https://youtu.be/I9cJuacpAiw """

url = 'https://upzerk.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
count = 0
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    count += 1
    x = 0
    try:
        print(source.find("meta", {"property": "og:image"}).attrs['content'])
        print(source.find("meta", {"property": "og:site_name"}).attrs['content'])
        print(source.find("meta", {"property": "og:type"}).attrs['content'])
        print(source.find("meta", {"property": "og:url"}).attrs['content'])
        print(source.find("meta", {"property": "og:title"}).attrs['content'])
    except:
        print(x)