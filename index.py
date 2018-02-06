import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "8") #Initialise client bot


@client.event 
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
  if message.content.upper().startswith('8PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content.upper().startswith('8ARGS'):
    args = message.content.split(" ")
    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

  if message.content.upper().startswith('8TEST'):
  
   botmsg = await client.send_message(message.channel, "Réaction d'un :baby_chick:")
   await client.add_reaction(botmsg, "🐤")

client.run("MzgxOTgxMjU2Mjg5NjE1ODgz.DVslCQ.mqpAYRXsItHvvNadAEeaYrQ8XX8") #Replace token with your bots token
