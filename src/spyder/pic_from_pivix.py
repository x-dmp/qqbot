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

