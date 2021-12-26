import os
import discord
from discord.ext import commands
import music
from keep_alive import keep_alive


my_key = os.environ['bot_key']
cogs = [music]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

keep_alive()
client.run(my_key)