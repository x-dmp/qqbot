from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import sys
# sys.path.append('/usr/local/qbot/bot/')
from src.main.utils.getPic import get_pic, get_pic_from_local


@on_command('setu', aliases=('涩图', '色图'))
async def setu(session: CommandSession):
    print('执行setu'+session.current_arg_text)
    res = ''
    if session.current_arg_text == '':
        src = get_pic_from_local()
        res = '恭喜你获得老婆一只！'
    else:
        try:
            src, quota = get_pic(r18=0, keyword=session.current_arg_text)
            if src == '-1':
                src = get_pic_from_local()
                print('api内部错误')
            elif src == '401':
                src = get_pic_from_local()
                print('由于不规范的操作而被拒绝调用')
            elif src == '403':
                src = get_pic_from_local()
                print('找不到符合关键字的色图')
            elif src == '429':
                src = get_pic_from_local()
                print('达到调用额度限制')
            await session.send('剩余服务次数：' + str(quota))
            res = '恭喜你获得' + session.current_arg_text.strip() +'老婆一只！'
        except Exception:
            src = get_pic_from_local()
            res = '网络受到神秘的非物质力量干扰，故老婆丢失，这边给您换了一个'
    await session.send(MessageSegment.image(src))
    await session.send(res+src)


# @on_natural_language(keywords={'涩图'}, only_to_me=True)
# async def _(session: NLPSession):
#     return IntentCommand(90.0, 'setu')
