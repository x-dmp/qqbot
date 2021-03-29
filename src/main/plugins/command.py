from nonebot import on_command, CommandSession


@on_command('command', aliases=('help', '?', '？', '帮助', ''))
async def weather(session: CommandSession):
    fp = open('./readme.txt', encoding='utf8')
    text = fp.read()
    await session.send(text)
