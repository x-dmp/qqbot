from selenium import webdriver
import time
import pyautogui as p
import os
import threading
import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'referer': 'https://www.pixiv.net/'
}


def get_pic(id: str, file_path: str):
    url = 'https://embed.pixiv.net/decorate.php?illust_id=' + id + '&mode=sns-automator'
    r = requests.get(url, headers=header)
    with open(file_path + id + '.png', 'wb+') as f:
        f.write(r.content)

# browser = webdriver.Chrome()
# browser.get('https://www.pixiv.net/')
# input()
# browser.set_page_load_timeout(10)
# local_dir = 'C:/Users/zwc/Desktop/ys/tmp/'
# store_dir = 'C:/Users/zwc/Desktop/ys/test/'
# lst = os.listdir(local_dir)
# for ii in lst:
#     s = ii.split('_')[0]
#     d = ''
#     dr = store_dir + d
#     url = 'https://www.pixiv.net/artworks/' + s
#     browser.maximize_window()
#     try:
#         browser.get(url)
#     except Exception:
#         pass
#     screenWidth, screenHeight = p.size()
#     p.moveTo(screenWidth / 2, screenHeight / 2)
#     p.rightClick()
#     p.moveRel(xOffset=20, yOffset=175)
#     p.click()
#     p.moveRel(xOffset=-220, yOffset=-200)
#     time.sleep(2)
#     p.press('enter')
