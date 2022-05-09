#Esta clase establece la conexion entre el bot y discord
import schedule
import time
import os
import discord
from fetchDB import tweet_info
TOKEN = 'Insert your own token'
client = discord.Client()
artists,links=tweet_info()
def fmensaje():
    @client.event
    async def background():
       global links,artists
       await client.wait_until_ready()
       channel = client.get_channel(int(756148847880700024))
       for i in range(len(links)):
                await channel.send(f'arista: {artists[i]}\n{links[i]}')
                comp=links[i]
                time.sleep(30)
       await client.close()
    client.loop.create_task(background())
    client.run(TOKEN)


fmensaje()
print('done so0')