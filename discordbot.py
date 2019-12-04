import discord
import os
import random
import get_moe_news

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

    if str(ctx.content).startswith('!moenews'):
        cmd_str = str(ctx.content).split(" ")

        if str(cmd_str[1:2]).strip() == "['all']":
            await ctx.channel.send('トップに表示されているニュースを全件表示します。')
            news = get_moe_news.get_moe_news(get_all=True)
        else:
            await ctx.channel.send('固定ニュース以外を表示します。')
            news = get_moe_news.get_moe_news(get_all=False)

        news_text = ""
        for d in news:
            news_text = news_text + d.get('title') + "\n"
            news_text = news_text + d.get('url') + "\n"
        await ctx.channel.send(news_text)

    if ctx.content == '!dice_test':
        await ctx.channel.send(f"{ctx.author.mention}はマジックダイスを振った！")

    if str(ctx.content).startswith('!dice'):
        cmd = str(ctx.content).split(' ')

        if cmd[0:1]:
            rand_min = int(cmd[1])
        else:
            rand_min = 0

        if cmd[1:2]:
            rand_max = int(cmd[2])
        else:
            rand_max = 1000

        dice = random.randint(rand_min, rand_max)
        await ctx.channel.send(ctx.author.mention + 'はマジックダイス' + '(' + str(rand_min) + '-' + str(rand_max) +')' + 'を振った！ ' + str(dice))

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
