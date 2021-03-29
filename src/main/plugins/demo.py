from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from src.main.utils.getPic import get_pic


@on_command('setu', aliases=('涩图', '色图'))
async def setu(session: CommandSession):
    print('执行setu')
    src, quoto = get_pic("95462828605c9b29d66cb3")
    await session.send(MessageSegment.image(src))


