# -*- coding: utf-8 -*-

from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


class command:
    command_name = 'None'
    command_aliases = {}
    has_args = False
    error_msg = ''

    def __init__(self, name, aliases, fun, has_args=False, error_msg='None params'):
        self.command_name = name
        self.command_aliases = aliases
        self.has_args = has_args
        self.error_msg = error_msg
        self.fun = fun

    @on_command(command_name, aliases=command_aliases)
    async def send_command(self, session: CommandSession, fun):
        await session.send(fun(session))

    @send_command.args_parser
    async def _(self, session: CommandSession):
        str = session.current_arg_text.strip()
        if session.is_first_run:
            if self.has_args and str:
                session.state['args'] = str
                return
            else:
                session.pause(self.error_msg)

