import discord
from discord.ext import commands
import os
import random
import traceback

bot = commands.Bot(command_prefix='d!')
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


@bot.command()
async def sou(ctx):
    with open('sou.txt') as d:
        l_dic = [s.strip() for s in d.readlines()]
    await ctx.send(random.choice(l_dic))


@bot.command()
async def ken(ctx):
    with open('ken.txt') as d:
        l_dic = [s.strip() for s in d.readlines()]
    await ctx.send(random.choice(l_dic))


@bot.event()
async def on_message(ctx):
    msg_list = ['こんばんは', 'こんにちは', 'おはよー']
    if ctx.author.bot:
        return
    if ctx.content in msg_list:
        await ctx.send('へいよーぐっつすっす')



bot.run(token)
