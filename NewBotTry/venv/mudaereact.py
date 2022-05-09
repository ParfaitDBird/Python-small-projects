import arttable_imp
import discord
import time
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import fetchDB
DISCORD_TOKEN = ''
#Prefix for the bot commands
bot = commands.Bot(command_prefix="$",case_insensitive=True)
emojis = ['Heart', 'UniLove', 'Watalove']
adminBug = bot.get_channel(733721953134837861)
message = await adminBug.send(embed=embed)

for emoji in emojis:
    await message.add_reaction(emoji)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error