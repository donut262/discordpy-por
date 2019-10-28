import discord
from discord.ext import commands
import os
import random
import traceback
# import get_moe_news

# bot = commands.Bot(command_prefix='d!')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

# with open('greeting.txt') as f:
#     greeting_list = [s.strip() for s in f.readlines()]


@client.event
async def on_ready():
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')


@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return

    # if ctx.content == '!moe_news all':
    #     news = get_moe_news.get_moe_news(get_all=True)
    #     news_text = "'''\n"
    #     for d in news:
    #         news_text = news_text + d.get('title') + "\n"
    #         news_text = news_text + d.get('url') + "\n"
    #     news_text = news_text + "'''"
    #     await ctx.channel.send(news_text)
    #
    # if ctx.content == '!moe_news':
    #     news = get_moe_news.get_moe_news(get_all=False)
    #     news_text = "'''\n"
    #     for d in news:
    #         news_text = news_text + d.get('title') + "\n"
    #         news_text = news_text + d.get('url') + "\n"
    #     news_text = news_text + "'''"
    #     await ctx.channel.send(news_text)

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

    # for row in greeting_list:
    #     if str(ctx.content).startswith(row):
    #         await ctx.channel.send(f"へいよーぐっつすっす\n{ctx.author.mention}さん、いらっしゃ～い")
    #         break


client.run(token)
