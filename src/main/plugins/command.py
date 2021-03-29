from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.message import MessageSegment
from src.main.utils.getPic import get_pic


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    src, quoto = get_pic('')
    print(MessageSegment.image(src))
    print(quoto)
    await session.send(MessageSegment.image(src))


@on_natural_language(keywords={'天气'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'weather')
