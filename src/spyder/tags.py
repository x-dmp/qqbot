import requests
from bs4 import BeautifulSoup
import json

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'referer': 'https://www.pixiv.net/'
}

url = 'https://www.pixiv.net/artworks/'


def get_tags(id:str) -> list:
    url_lst = url + id + '?lang=zh'
    response = requests.get(url_lst, headers=header)
    soup = BeautifulSoup(response.text)
    tags_org = soup.find_all('meta', attrs={'id': 'meta-preload-data'})
    try:
        data = json.loads(tags_org[0]['content'])
        data = data['illust'][id]['tags']['tags']
        res = []
        for ii in data:
            try:
                print(ii['translation']['en'])
                print(ii['tag'])
                res.append(ii['translation']['en'])
                res.append(ii['tag'])
            except Exception:
                pass
        return res
    except Exception:
        pass