#Esta clase establece la conexion entre el bot y discord
import schedule
import time
import os
import discord
from Twittah import tweet_info
TOKEN = 'Insert your own token'
client = discord.Client()
artists,links=tweet_info()
f = open("Enlaces.txt", "r")
comp = f.readline()
f.close()
def actualizar_txt(link):
    f = open("Enlaces.txt", "w")
    f.write(link)
    f.close()
def fmensaje():
    @client.event
    async def background():
       global comp,links,artists
       await client.wait_until_ready()
       channel = client.get_channel(int(756148847880700024))
       for i in range(len(links)):
            if(comp!=links[i]):
                await channel.send(f'arista: {artists[i]}\n{links[i]}')
                actualizar_txt(str(links[i]))
                comp=links[i]
                time.sleep(30)
            else:
                print("No updates")
       await client.close()
    client.loop.create_task(background())
    client.run(TOKEN)
fmensaje()
print('done so0')