import requests
from PIL import Image
import json
from io import BytesIO
import os
import time

id = '516035062'
offset = ''
url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=' + id + '&offset_dynamic_id='
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'referer': 'https://space.bilibili.com/' + id + '/dynamic'
}
local_dir = 'C:/Users/zwc/Desktop/pic6/'
pic_num = os.listdir(local_dir).__len__()
pic_num += 1
res = requests.get(url+offset, header)
while True:
    data = res.json()
    cards = data['data']['cards']
    for card in cards:
        content = card['card']
        if content.__contains__('饿了么'):
            continue
        if content.__contains__('美团'):
            continue
        if content.__contains__('公众号') or content.__contains__('单抽') or content.__contains__('0元白嫖') or content.__contains__('群'):
            continue
        c = json.loads(card['card'])
        if 'item' not in c:
            continue
        if 'pictures' in c['item']:
            pictures = c['item']['pictures']
            for picture in pictures:
                if 'img_src' in picture:
                    img_url = picture['img_src']
                    try:
                        img = requests.get(img_url)
                        img_cache = Image.open(BytesIO(img.content))
                        img_cache.save(local_dir + str(pic_num) + '.png')
                        pic_num += 1
                    except Exception:
                        print('pic not exist')
                        continue

    time.sleep(5)
    print('download for one batch')
    print('totle is ' + str(pic_num))
    res = requests.get(url + str(data['data']['next_offset']), header)
    print('currant url: ' + url + str(data['data']['next_offset']))