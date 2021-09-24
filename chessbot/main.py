from discord.ext import commands
import discord
from config import TOKEN
from function import get_elo, live_game

# Set command prefix
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.command(name='rapid')
async def get_rapid(ctx, user):
    """ The function returns the rapid rating.  """
    try:
        await ctx.send(f"{user}s rapid rating on Lichess is ", get_elo(user, "rapid"))
    except Exception as error:
        await ctx.send("Unfortunately an error has occurred")
        await ctx.send(f"Error:: {error}")


@bot.command(name='blitz')
async def get_blitz(ctx, user):
    """ The function returns the blitz rating.  """
    try:
        await ctx.send(f"{user}s blitz rating on Lichess is ", get_elo(user, "blitz"))
    except Exception as error:
        await ctx.send("Unfortunately an error has occurred")
        await ctx.send(f"Error:: {error}")


@bot.command(name='bullet')
async def get_bullet(ctx, user):
    """ The function returns the bullet bullet.  """
    try:
        await ctx.send(f"{user}s bullet rating on Lichess is ", get_elo(user, "bullet"))
    except Exception as error:
        await ctx.send("Unfortunately an error has occurred")
        await ctx.send(f"Error:: {error}")


@bot.command(name='live')
async def get_live_game(ctx, user):
    """ The function returns the live game.  """
    try:
        await ctx.send(f"Here you can find the live game of {user}:", live_game(user))
    except Exception as error:
        await ctx.send("Unfortunately an error has occurred")
        await ctx.send(f"Error:: {error}")

bot.run(TOKEN)
