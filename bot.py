import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix = 'f.', self_bot = True)
# IMPORTANT!
# Change The Prefix f. To Anything You Want
# Change Owner ID To Your ID 

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
        if config.get('TOKEN') == "LOL":
            if not os.environ.get('TOKEN'):
                print("Navigate To config.json in data folder and add your token or add A TOKEN config var in heroku")
        else:
            token = config.get('TOKEN').strip('\"')
    return os.environ.get('TOKEN') or token

@bot.command()
async def Ping(ctx):
    """Pong! Check If Bot Is Working"""
    await ctx.send("Pong!")
    
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
