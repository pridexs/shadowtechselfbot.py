import discord
import os
import io
from discord.ext import commands
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


@bot.event
async def on_ready():
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
                run_wizard()
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
    return os.environ.get('PREFIX') or prefix or 'cr.'

@bot.command()
async def Ping(ctx):
    """Pong! Check If Bot Is Working"""
    await ctx.send("Pong!")
    
# if not os.environ.get('TOKEN'):
#   print("no token found REEEE!")
# bot.run(os.environ.get('TOKEN').strip('\"'))
# turning them in to comments now might need it later  
