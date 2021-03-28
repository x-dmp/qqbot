# -*- coding: utf-8 -*-
import nonebot
import src.main.config as config
import os

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run()