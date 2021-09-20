import os
import urllib
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set command prefix
bot = commands.Bot(command_prefix='!')
@bot.command(name='elo')

#arg1: game type i.e. blitz or rapid
#arg2: player name
async def get_rapid_elo(ctx, arg1, arg2):
    # Build the lichess url and open it
    lichess_url = 'https://lichess.org/api/user/' + str(arg2)
    j = urllib.request.urlopen(lichess_url)
   
    # returns JSON object as a dictionary
    player_data = json.load(j)

    response = f"{arg2}s {arg1} rating auf Lichess ist: " + str(player_data["perfs"][str(arg1)]["rating"])
    await ctx.send(response)

bot.run(TOKEN)