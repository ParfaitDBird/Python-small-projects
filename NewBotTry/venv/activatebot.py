import arttable_imp
import discord
import time
import asyncio
import random
from discord.ext import commands
import fetchDB
TOKEN = ''
client = discord.Client()

client = commands.Bot(command_prefix="$")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$off'):
        await client.wait_until_ready()
        channel = client.get_channel(int(756148847880700024))
        await channel.send('See ya later horny motherfuckers! :)')
        await client.close()
    # Detects if user wants to receive all images from database ( over 1000 messages )

    if message.content.startswith('$fetch'):
        await client.wait_until_ready()
        channel = client.get_channel(int(756148847880700024))
        await channel.send('Database will be updated, please wait 5 minutes.')
        fetchDB.fetchdb()
        await  channel.send('Database has been updated.')
    if (message.content.startswith('$ALL') or message.content.startswith('$All') or message.content.startswith('$all')):
        try:
            initialuser = message.author
            start = time.time()
            await client.wait_until_ready()
            channel = client.get_channel(int(756148847880700024))
            await channel.send('This process will take a long time to complete so just enjoy and discover some yabe art.')
            nsfwtable = arttable_imp.listado.nsfw()
            for i in range(len(nsfwtable)):
                await channel.send(f'Artist: {nsfwtable[i][0]}\n{nsfwtable[i][1]}')
                time.sleep(3)
            end = time.time()
            await channel.send(f'Final image reached {initialuser}\nTime elapsed: {end - start}')
        except:
            print('Error occurred.')
    #Detects if user wants to receive nsfw images custom amount
    if ((message.content.startswith('$NSFW') or message.content.startswith('$nsfw') or message.content.startswith('$Nsfw'))):
        try:
            initialuser= message.author
            await client.wait_until_ready()
            channel = client.get_channel(int(756148847880700024))
            await channel.send('Num images: ____')
            def valmess(m):
                return m.author == initialuser
            response = await client.wait_for('message', check=valmess, timeout=7.0)
            nsfwtable = arttable_imp.listado.nsfw()
            cont = 0
            print(len(nsfwtable))
            while cont < int(response.content):
                i=random.randint(0, len(nsfwtable)-1)
                await channel.send(f'Artist: {nsfwtable[i][0]}\n{nsfwtable[i][1]}')
                time.sleep(3)
                cont+=1
            await channel.send(f'Final image reached {initialuser}.')
        except ValueError:
            await channel.send('Send a number and try again.')
        except asyncio.TimeoutError:
            await channel.send('Make up your mind :(')
        except IndexError:
            await channel.send('Unexpected error with range')
    #Detects if user wants some specific artist allows amount input.
    if (message.content.startswith(r'$Artist') or message.content.startswith('$ARTIST') or message.content.startswith('$artist')):
        try:
            initialuser = message.author
            await client.wait_until_ready()
            channel = client.get_channel(int(756148847880700024))
            await channel.send('Which artist?')
            time.sleep(0.1)
            def valmess(m):
                return m.author == initialuser
            response = await client.wait_for('message',check=valmess, timeout=12.0)
            artist = arttable_imp.validacionArtist(response.content)
            if artist:
                await channel.send('How many images?')
                time.sleep(0.1)
                nresponse = await client.wait_for('message', check=valmess, timeout=7.0)
                nsfwtable = arttable_imp.artistlist.artlist(int(''.join(filter(str.isdigit, nresponse.content))),
                                                            response.content)
                for i in range(len(nsfwtable)):

                    await channel.send(f'Artist: {nsfwtable[i][0]}\n{nsfwtable[i][1]}')
                    time.sleep(3)
                await channel.send(f'Final image reached {initialuser}.')
            else:
                print(artist)
                await  channel.send('Artist not found.')
            #  await client.close()
        except ValueError:
            await channel.send('Send a number and try again.')
        except asyncio.TimeoutError:
            await channel.send('Decide an amount and try again.')
    #Adds image to DB from message
    if message.content.startswith('$add') or message.content.startswith('$Add') or message.content.startswith('$ADD'):
        try:
            initialuser = message.author
            url = False
            await client.wait_until_ready()
            channel = client.get_channel(int(756148847880700024))
            await channel.send('Send image to add:')
            nresponse = await client.wait_for('message', timeout=10.0)
            if nresponse.attachments:
                url = nresponse.attachments[0].url
            elif str(nresponse.content):
                url = nresponse.content
            await channel.send('Artist: (dont answer if you do not know it.)')
            author = await  client.wait_for('message', timeout=10.0)
            author = str(author.content)
            arttable_imp.discordattachment(url,author)
            await channel.send('Added to database')
        except asyncio.TimeoutError:
            if url:
                author = 'Unknown'
                arttable_imp.discordattachment(url,author)
                await channel.send('Added to database')
            else:
                await channel.send('Could not add to the database')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
#                for i in range(len(nsfwtable)):
