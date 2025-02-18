import discord
import os
client=discord.Client()

@client.event
async def on_ready():
   print('Welcome')
@client.event
async def on_message(messsage):
  if messsage.author==client.user:
    return 
  if messsage.content.startswith('!details'):
    await messsage.channel.send(" Name: Raihan Rahman ")

client.run(os.getenv('T'))
 
