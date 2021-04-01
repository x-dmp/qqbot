from src.spyder import tags
import src.main.pysql.pysql_test as pysql
import os


def get_tag(tag_list):
    tag_re = ''
    for t in tag_list:
        tag_re = tag_re + t + '_'
    return tag_re


def get_local_dir(id: str, local_dir: str) -> str:
    d = ''
    for j in id:
        d = d + j + '/'
        if not os.path.exists(local_dir + d):
            os.mkdir(local_dir + d)
    return local_dir + d


def store_pic_by_id(uid, local_dir, d):
    tag_list = tags.get_tags(uid)
    if tag_list is None:
        return
    tag_re = get_tag(tag_list)
    pysql.insert_pic(uid, d, tag_re)
