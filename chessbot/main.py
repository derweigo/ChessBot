from lichesspy.api import user as liuser
from discord.ext import commands
import discord
from config import TOKEN

# Set command prefix
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.command(name='elo')
async def get_elo(ctx, arg1, arg2):
    """ 
        The function returns the Lichess rating of the searched player.
    """
    try:

        # Loads all information of the user into the variable
        user = liuser(arg1)['perfs'][arg2]['rating']

        # Sends the message to the channel
        await ctx.send(f"{arg1}s {arg2} rating auf Lichess ist: {user}")
    except Exception as error:
        await ctx.send("Leider ist ein Fehler aufgetreten.")
        await ctx.send(f"Fehler: {error}")

bot.run(TOKEN)
