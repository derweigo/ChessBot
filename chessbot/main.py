from discord.ext import commands
import discord
from config import TOKEN
from function import get_elo

# Set command prefix
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.command(name='rapid')
async def get_rapid(ctx, user):
    """ The function returns the rapid rating.  """
    try:
        await ctx.send(f"{user}s rapid rating on Lichess is ", get_elo(user, "rapid"))
    except Exception as error:
        await ctx.send("Leider ist ein Fehler aufgetreten.")
        await ctx.send(f"Fehler: {error}")

@bot.command(name='blitz')
async def get_rapid(ctx, user):
    """ The function returns the blitz rating.  """
    try:
        await ctx.send(f"{user}s rapid rating on Lichess is ", get_elo(user, "blitz"))
    except Exception as error:
        await ctx.send("Leider ist ein Fehler aufgetreten.")
        await ctx.send(f"Fehler: {error}")

@bot.command(name='bullet')
async def get_rapid(ctx, user):
    """ The function returns the rapid bullet.  """
    try:
        await ctx.send(f"{user}s rapid rating on Lichess is ", get_elo(user, "bullet"))
    except Exception as error:
        await ctx.send("Leider ist ein Fehler aufgetreten.")
        await ctx.send(f"Fehler: {error}")


bot.run(TOKEN)
