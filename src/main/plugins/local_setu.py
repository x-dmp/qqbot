from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import sys
# sys.path.append('/usr/local/qbot/bot/')
from src.main.utils.getPic import get_pic, get_pic_from_local, get_pic_from_sql
from src.main.utils.random_pic import get_random_src
import src.main.utils.option as option

def isnumber(s):
    try:
        int(s)
        return True
    except Exception:
        pass


@on_command('setu_local', aliases=('图', 't'))
async def setu(session: CommandSession):
    print('执行setu' + session.current_arg_text)
    res = ''
    code = 0
    if session.current_arg_text == '':
        src = get_random_src(option.get_option()['sql_dir'])
        res = '恭喜你获得老婆一只！'
        print(src)
        await session.send(MessageSegment.image(src), at_sender=True)
        await session.send(res, at_sender=True)
    else:
        s = session.current_arg_text
        if isnumber(s):
            num = int(session.current_arg_text)
            if num >= 10:
                await session.send('做人不能太贪心哦！', at_sender=True)
                num = 1
            for i in range(num):
                src = get_random_src(option.get_option()['sql_dir'])
                await session.send(MessageSegment.image(src), at_sender=True)
            res = '共计获得老婆' + str(num) + '只！'
            await session.send(res, at_sender=True)
        else:
            try:
                src = get_pic_from_sql(session.current_arg_text)
                res = '恭喜你获得' + session.current_arg_text.strip() + '老婆一只！'
            except Exception:
                src = get_random_src(option.get_option()['sql_dir'])
                res = '网络受到神秘的非物质力量干扰，故老婆丢失，这边给您换了一个'
            await session.send(MessageSegment.image(src), at_sender=True)
            await session.send(res, at_sender=True)
