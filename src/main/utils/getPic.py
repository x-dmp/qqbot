import requests
from PIL import Image
import sys
import random
# sys.path.append('/usr/local/qbot/bot/')
import src.main.utils.option as option
from io import BytesIO
import os


def get_pic(r18=0, keyword='') -> tuple:
    opt = option.get_option()
    url = opt['web_url'] + '?r18=' + str(r18) + '&size1200=true' + '&apikey=' + opt['apikey'] + '&keyword=' + keyword
    response = requests.get(url)
    data = response.json()
    quota = data['quota']
    code = data['code']
    if code == 429:
        return '429', quota
    elif code == -1:
        return '-1', quota
    elif code == 401:
        return '401', quota
    elif code == 404:
        return '404', quota
    elif code == 403:
        return '403', quota
    pic_url = data['data'][0]['url']
    img_name = pic_url.split('/')[-1]
    loc = opt['cache_dir'] + img_name
    if not os.path.exists(loc):
        print("本地无图片，开始下载")
        img = requests.get(pic_url)
        img_cache = Image.open(BytesIO(img.content))
        img_cache.save(loc, quality=80)
        print("下载完成")
    return loc, quota


def get_pic_from_local() -> str:
    opt = option.get_option()
    location = random.randint(1, opt['local_pic_num'])
    url = opt['local_dir'] + 'photo_' + str(location) +'.jpg'
    return url