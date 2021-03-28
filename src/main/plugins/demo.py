from nonebot import on_command, CommandSession

@on_command('setu', aliases=('涩图', '色图'))
async def setu(session: CommandSession):
    print('执行setu')
    print(session.current_arg_text)
    await session.send('收到涩图命令')


