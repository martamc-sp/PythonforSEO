import requests
from bs4 import BeautifulSoup
""" https://www.youtube.com/watch?v=PzWIdcFY9YQ """
url = 'https://url.com/sitemap.xml'
sitemapsoup = BeautifulSoup(requests.get(url).content, 'lxml')
sitemapurls = sitemapsoup.find_all("loc")
xml_urls = [sitemapurl.text for sitemapurl in sitemapurls]
count = 0
cerror = 0
mydata = open("FILEPATH/data.txt", "w")
for websiteurls in xml_urls:
    source = BeautifulSoup(requests.get(websiteurls).text , 'html.parser')
    try:
        count += 1
        mydata.write("yes!")
        mydata.write("\n")
        mydata.write(source.find('link', {'rel': 'canonical'}) ['href'])
        mydata.write("\n")
        print(count)
    except:
        mydata.write("no!")
        mydata.write(websiteurls)
        cerror += 1
        print(cerror)
mydata.close()
