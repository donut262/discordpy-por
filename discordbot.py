from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


async def chum(ctx):
    await ctx.send('にゅたこのおぱんつ見たいな・・・')


bot.run(token)
