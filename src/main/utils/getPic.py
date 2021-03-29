import requests
from PIL import Image
import src.main.config as opt
from io import BytesIO


def get_pic(apikey: str, r18=0) -> tuple:
    # url = opt.web_url + '?' + 'apikey=' + apikey + '&r18=' + str(r18) + '&size1200=true'
    url = opt.web_url + '?r18=' + str(r18) + '&size1200=true' + '&apikey=' + apikey
    # url = opt.web_url + '?r18=' + str(r18) + '&size1200=true'
    response = requests.get(url)
    data = response.json()
    quota = data['quota']
    pic_url = data['data'][0]['url']
    img = requests.get(pic_url)
    img_name = pic_url.split('/')[-1]
    img_cache = Image.open(BytesIO(img.content))
    loc = opt.cache_dir + img_name
    img_cache.save(loc, quality=100)
    return loc, quota
