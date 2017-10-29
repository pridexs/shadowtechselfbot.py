import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix = 'f.', self_bot = True)
# IMPORTANT!
# Change The Prefix f. To Anything You Want
# Change Owner ID To Your ID 

async def on_ready:
    print("Selfbot Online And Succesfully Installed")
    print("_________________________")
    print("Creator: Free TNT#5796")
    
@bot.command()
async def Ping(ctx):
    """Pong! Check If Bot Is Working"""
    await ctx.send("Pong!")
    
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
