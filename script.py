import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def test(ctx, arg):
    await ctx.send('hello')

@bot.command()
async def hi(ctx):
    await ctx.send('Hello ' + str(ctx.author.name) + '! :)')

bot.run(DISCORD_TOKEN)
