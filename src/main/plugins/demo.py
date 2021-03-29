from nonebot import on_command, CommandSession

@on_command('setu', aliases=('涩图', '色图'))
async def setu(session: CommandSession):
    print('执行setu')
    keyword = session.current_arg_text
    apikey = '95462828605c9b29d66cb3'
    size1200 = True
    r18 = 0

    await session.send('收到涩图命令')


