
def get_dir(uid):
    dir=''
    for c in uid:
        if dir == '':
            dir = c + '\\'
        else:
            dir = dir + c + '\\'
    return dir
