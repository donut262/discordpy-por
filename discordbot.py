import discord
from discord.ext import commands
import os
import random
import traceback
import re
from bs4 import BeautifulSoup
import urllib.request, urllib.error
from xml.sax.saxutils import unescape

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

official_url = 'https://moepic.com'


# with open('greeting.txt') as f:
#     greeting_list = [s.strip() for s in f.readlines()]

def get_moe_news(get_all=True):
    except_list = []
    if get_all is False:
        with open('except_news_titles.txt', mode='rb') as f:
            except_list = [s.strip() for s in f.readlines()]

    # HTMLのパース
    html = urllib.request.urlopen(official_url + '/top.php?mid=_')
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('a', class_='topnews_imp')
    news_list = []

    # topnews_impクラスが存在する場合のみ処理
    if len(news) > 0:
        # タイトルとURLを取り出してリストに入れる
        for row in news:
            pat = "^.+href=\"javascript:Move\(\'(.+)\',\'(.+)\'\)\">(.+)<\/a>"
            repatter = re.compile(pat)
            result = repatter.match(str(row))

            # パターンにマッチした場合だけ処理を実行
            if result is not None:
                url = official_url + result.group(1) + '?hidden_key=' + result.group(2)
                title = unescape(result.group(3))
                news_list.append({'title': title, 'url': url})

    output_list = []
    for d in news_list:
        news_title = d.get('title').encode('utf-8')
        if news_title not in except_list:
            output_list.append(d)

    return output_list


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

    if ctx.content == '!moe_news':
        news = get_moe_news.get_moe_news(get_all=False)
        news_text = "'''\n"
        for d in news:
            news_text = news_text + d.get('title') + "\n"
            news_text = news_text + d.get('url') + "\n"
        news_text = news_text + "'''"
        await ctx.channel.send(news_text)

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
