import requests
from bs4 import BeautifulSoup
name = '龙与虎'
url = 'https://api.bilibili.com/x/web-interface/search/type?context=&page=1&keyword='+ name +'&search_type=video'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'referer': 'https://space.bilibili.com/'
}
r = requests.get('https://search.bilibili.com/all?keyword='+name, headers=header)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
result = soup('div')
re = str(soup.find_all('a', class_="left-img")[0]).split('/')[5]
print(re)