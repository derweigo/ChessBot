import urllib
import json
from discord.ext import commands
from config import TOKEN
import lichesspy.api as lichess

# Set command prefix
bot = commands.Bot(command_prefix='!')


@bot.command(name='elo')
async def get_elo(ctx, arg1, arg2):
   """ 
        The function returns the Lichess rating of the searched player.
    """

   # Loads all information of the user into the variable
   user = lichess.user(arg1)['perfs'][arg2]['rating']
   
   # Sends the message to the channel
   await ctx.send(f"{arg1}s {arg2} rating auf Lichess ist: {user}")

bot.run(TOKEN)
