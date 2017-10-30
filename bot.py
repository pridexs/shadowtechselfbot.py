import discord
import os
import io
from discord.ext import commands
import re
import sys
import json
import aiohttp
import psutil
# bot = commands.Bot(command_prefix = 'f.', self_bot = True)
# IMPORTANT!
# Change The Prefix f. To Anything You Want
# Change Owner ID To Your ID 
# Nvm ignore it 

class Selfbot(commands.Bot):
    '''A Discord Selfbot Made By Free TNT#5796'''
    _mentions_transforms = {
        '@everyone': '@\u200beveryone',
        '@here': '@\u200bhere'
    }

    _mention_pattern = re.compile('|'.join(_mentions_transforms.keys()))

    def __init__(self, **attrs):
            super().__init__(command_prefix=self.get_pre, self_bot=True)
            self.session = aiohttp.ClientSession(loop=self.loop)
            self.process = psutil.Process()
            self._extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
            self.last_message = None
            self.messages_sent = 0
            self.commands_used = defaultdict(int)
            self._add_commands()
            self.load_extensions()

    def _add_commands(self):
        '''Adds commands automatically'''
        for attr in dir(self):
            cmd = getattr(self, attr)
            if isinstance(cmd, commands.Command):
                self.add_command(cmd)

    def load_extensions(self, cogs=None, path='cogs.'):
        '''Loads the default set of extensions or a separate one if given'''
        for extension in cogs or self._extensions:
            try:
                self.load_extension(f'{path}{extension}')
                print(f'Loaded extension: {extension}')
            except Exception as e:
                print(f'LoadError: {extension}\n'
                      f'type(e).__name__: {e}')


    async def on_ready(self):
        print("Selfbot Online And Succesfully Installed")
        print("_________________________")
        print("Creator: Free TNT#5796")
    
    @property
    def token():
        '''Returns your token wherever it is'''
        with open('data/config.json') as f:
            config = json.load(f)
            if config.get('TOKEN') == "your_token_here":
                if not os.environ.get('TOKEN'):
                    self.run_wizard()
            else:
                token = config.get('TOKEN').strip('\"')
        return os.environ.get('TOKEN') or token

    @classmethod
    def init(bot, token=None):
        '''Starts the actual selfbot'''
        selfbot = bot()
        safe_token = token or selfbot.token.strip('\"')
        try:
            selfbot.run(safe_token, bot=False, reconnect=True)
        except Exception as e:
            print(e)

    @staticmethod
    async def get_pre(bot, message):
        '''Returns the prefix'''
        with open('data/config.json') as f:
            prefix = json.load(f).get('PREFIX')
        return os.environ.get('PREFIX') or prefix or 'f.'

    @commands.command()
    async def Ping(self, ctx):
        """Pong! Check If Bot Is Working"""
        await ctx.send("Pong!")
    
if __name__ == '__main__':
    Selfbot.init()

# if not os.environ.get('TOKEN'):
#   print("no token found REEEE!")
# bot.run(os.environ.get('TOKEN').strip('\"'))
# turning them in to comments now might need it later  
