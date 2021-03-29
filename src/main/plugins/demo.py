from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import sys
# sys.path.append('/usr/local/qbot/bot/')
from src.main.utils.getPic import get_pic


@on_command('setu', aliases=('涩图', '色图'))
async def setu(session: CommandSession):
    print('执行setu'+session.current_arg_text)
    src, _ = get_pic(r18=0, keyword=session.current_arg_text)
    await session.send(MessageSegment.image(src))


# @on_natural_language(keywords={'涩图'}, only_to_me=True)
# async def _(session: NLPSession):
#     return IntentCommand(90.0, 'setu')
