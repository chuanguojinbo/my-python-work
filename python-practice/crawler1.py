#it is a historical moment
import requests
from lxml import html
url='https://movie.doubancom/'
page=requests.Session().get(url)
tree=html.fromstring(page.text)
result=tree.xpath('//td[@class="title"]//a/text()')
print(result)