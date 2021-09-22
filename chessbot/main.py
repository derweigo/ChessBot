import lichesspy.api as lichess
from discord.ext import commands
from config import TOKEN

# Set command prefix
bot = commands.Bot(command_prefix='!')


@bot.command(name='elo')
async def get_elo(ctx, arg1, arg2):
    """ 
        The function returns the Lichess rating of the searched player.
    """
    try:

        # Loads all information of the user into the variable
        user = lichess.user(arg1)['perfs'][arg2]['rating']

        # Sends the message to the channel
        await ctx.send(f"{arg1}s {arg2} rating auf Lichess ist: {user}")
    except Exception as e:
        await ctx.send("Leider ist ein Fehler aufgetreten.")
        await ctx.send(f"Fehler: {e}")

bot.run(TOKEN)
