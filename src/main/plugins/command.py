from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.message import MessageSegment
import numpy as np


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    pic = 'tmp/ys.png'
    print(pic)

    await session.send(MessageSegment.image(pic))


@on_natural_language(keywords={'天气'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'weather')
