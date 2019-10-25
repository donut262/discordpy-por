import discord
from discord.ext import commands
import os
import random
import traceback

# bot = commands.Bot(command_prefix='d!')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(ctx):
    msg_list = ['こんばんは', 'こんにちは', 'おはよー', 'ばんちゃー']
    if ctx.author.bot:
        return
    if ctx.content == '!chum':
        with open('chum.txt') as d:
            l_dic = [s.strip() for s in d.readlines()]
        await ctx.channel.send(random.choice(l_dic))
    if ctx.content == '!sou':
        with open('sou.txt') as d:
            l_dic = [s.strip() for s in d.readlines()]
        await ctx.channel.send(random.choice(l_dic))
    if ctx.content == '!ken':
        with open('ken.txt') as d:
            l_dic = [s.strip() for s in d.readlines()]
        await ctx.channel.send(random.choice(l_dic))
    if ctx.content in msg_list:
        await ctx.channel.send('へいよーぐっつすっす')


client.run(token)
