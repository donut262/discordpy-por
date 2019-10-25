from discord.ext import commands
import os
import random
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def chum(ctx):
    with open('chum.txt') as d:
        l_dic = [s.strip() for s in d.readlines()]
    await ctx.send(random.choice(l_dic))


bot.run(token)
