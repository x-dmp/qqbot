import requests
from PIL import Image
import sys
import random
# sys.path.append('/usr/local/qbot/bot/')
import src.main.config as opt
from io import BytesIO
import os


def get_pic(apikey: str, r18=0) -> tuple:
    url = opt.web_url + '?r18=' + str(r18) + '&size1200=true' + '&apikey=' + apikey
    response = requests.get(url)
    data = response.json()
    quota = data['quota']
    pic_url = data['data'][0]['url']
    img_name = pic_url.split('/')[-1]
    loc = opt.cache_dir + img_name
    if not os.path.exists(loc):
        img = requests.get(pic_url)
        img_cache = Image.open(BytesIO(img.content))
        img_cache.save(loc, quality=80)
    return loc, quota


def get_pic() -> str:
    location = random.randint(1, 1000)
    url = opt.local_dir + 'photo_' + str(location) +'.jpg'
    print(url)
    return url