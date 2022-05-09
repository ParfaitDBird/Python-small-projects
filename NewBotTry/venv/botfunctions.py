import arttable_imp
import discord
import time
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import fetchDB
DISCORD_TOKEN = 'Insert your own token
#Prefix for the bot commands
bot = commands.Bot(command_prefix="$",case_insensitive=True)

# Detects if user wants to receive  images custom amount
@bot.command()
async def nsfw(ctx, args=''):
    try:
        if int(args)>0:
            author = ctx.author
            nsfwtable = arttable_imp.listado.nsfw()
            cont = 0
            print(len(nsfwtable))
            while cont < int(args):
                i = random.randint(0, len(nsfwtable) - 1)
                await ctx.channel.send(f'Artist: {nsfwtable[i][0]}\n{nsfwtable[i][1]}')
                print(f'{cont})Antes del pop \n {i} {len(nsfwtable)}')
                nsfwtable.pop(i)
                print(f'{cont})despues del pop \n {i} {len(nsfwtable)}')
                await asyncio.sleep(3)
                cont += 1
            await ctx.channel.send(f'Final image reached {author}')
        else:
            await ctx.channel.send('command is $nsfw [amount]')
    except ValueError:
        await ctx.channel.send('Send a number and try again.')
    except IndexError:
        await ctx.channel.send('Unexpected error with range')
    except MissingRequiredArgument:
        await ctx.channel.send('Command is $nsfw [amount of images]')

#Adds an image to the DB
@bot.command()
async def add(ctx, args=''):
    try:
        url = ''
        await ctx.channel.send('Send image to add:')
        nresponse = await bot.wait_for('message', timeout=10.0)
        if nresponse.attachments:
            url = nresponse.attachments[0].url
        elif str(nresponse.content):
            url = nresponse.content
        await ctx.channel.send('Artist: (dont answer if you do not know it.)')
        author = await  bot.wait_for('message', timeout=10.0)
        author = str(author.content)
        arttable_imp.discordattachment(url, author)
        await ctx.channel.send('Added to database')
    except asyncio.TimeoutError:
        if url:
            author = 'Unknown'
            arttable_imp.discordattachment(url, author)
            await ctx.channel.send('Added to database')
        else:
            await ctx.channel.send('Could not add to the database')
    except MissingRequiredArgument:
        await ctx.channel.send('and url or attachment is required.')


@bot.command()
async def fetch(ctx):
    await ctx.channel.send('Database will be updated, please wait 5 minutes.')
    fetchDB.fetchdb()
    await  ctx.channel.send('Database has been updated.')



@bot.command()
async def artist(ctx,args=''):
    try:
        if arttable_imp.validacionArtist(args):
            author = ctx.author
            time.sleep(0.1)
            def valmess(m):
                return m.author == author

            await ctx.channel.send('How many images?')
            time.sleep(0.1)
            nresponse = await ctx.bot.wait_for('message', check=valmess, timeout=7.0)
            nsfwtable = arttable_imp.artistlist.artlist(int(''.join(filter(str.isdigit, nresponse.content))),args)
            for i in range(len(nsfwtable)):
                await ctx.channel.send(f'Artist: {nsfwtable[i][0]}\n{nsfwtable[i][1]}')
                #list.remove(element)
                nsfwtable.pop(i)
                await asyncio.sleep(3)
            await ctx.channel.send(f'Final image reached {author}.')
        else:
            await  ctx.channel.send('Artist not found.')
    except ValueError:
        await ctx.channel.send('Send a number and try again.')
    except asyncio.TimeoutError:
        await ctx.channel.send('Decide an amount and try again.')

@bot.command()
async def all(ctx):
    try:
        start = time.time()
        author = ctx.author
        def valmess(m):
            print(m)
            return m.author == author
        table = arttable_imp.listado.nsfw()
        await ctx.channel.send(f'This will take a long time to complete, so just enjoy from time to time.\n'
                               f' Sending {len(table)} images')
        for i in range(len(table)):
            await ctx.channel.send(f'Artist: {table[i][0]}\n{table[i][1]}')
            time.sleep(3)
        await ctx.channel.send('Final image reached.')
    except asyncio.TimeoutError:
        print("No stop message issued")



@bot.command()
async def off(ctx):
    await ctx.channel.send('Later motherfuckers! :)')
    await bot.close()
#Dumb extras
@bot.command()
async def ahoy(ctx):
    await ctx.channel.send('AHOOOOY! HOUSHOU MARINE DESUUUUU')
@bot.command()
async def polmao(ctx):
    await ctx.channel.send('Polka oru ka? oru yo!')
@bot.command()
async def w(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
@bot.command()
async def wa(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
@bot.command()
async def wb(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
@bot.command()
async def k(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
@bot.command()
async def daily(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
@bot.command()
async def wg(ctx):
    await ctx.channel.send('THIS ISNT MUDAE YOU DASTARD')
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


bot.run(DISCORD_TOKEN)

