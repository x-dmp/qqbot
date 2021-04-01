from src.spyder import tags, pic_from_pivix
import src.main.pysql.pysql_test as pysql


def save(id, src):
    pic_from_pivix.get_pic(id, src)
    return tags.get_tags(id)


def get_tag(tag_list):
    tag_re = ''
    for t in tag_list:
        tag_re = tag_re + t + '_'
    return tag_re


def store_pic_by_id(uid, local_dir, d):

    tag_list = save(uid, local_dir)
    if tag_list is None:
        return
    tag_re = get_tag(tag_list)
    pysql.insert_pic(uid, d, tag_re)
