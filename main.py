from keep_alive import keep_alive
import os
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("I'm in")
  print(client.user)


@client.event
async def on_message(message):
  if message.author != client.user:
    await message.channel.send(message.content[::-1])

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
