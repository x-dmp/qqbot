import json


def get_option():
    fp = open('./config', encoding='utf8')
    text = fp.read()
    return json.loads(text)