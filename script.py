import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='-')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def hi(ctx):
    await ctx.send('Hello ' + str(ctx.author.name) + '! :)')

bot.run(DISCORD_TOKEN)
