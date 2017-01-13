#!/usr/bin/python
import discord
import os.path
import aiohttp
import asyncio
from time import ctime


client = discord.Client()

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def clear_chat_channel(message):
    counter = 0
    all_messages = client.messages
    target_channel = message.channel
    for message_step in all_messages:
        if message_step.channel == target_channel:
            client.delete_message(message_step)
            counter += 1
    client.send_message(message.channel, 'I have removed %s old messages' % counter)
#
async def quit(message):
  await client.send_message(message.channel, "QUER MESMO SAIR ?(y/n)")

async def time(message):
  time = ctime()
  await client.send_message(message.channel, time)
#
async def say(message):
   say = message.content.strip("/say")
   await client.send_message(message.channel, say)


#

async def xingar(message):
   pessoa = message.content.strip("/xingar")
   marcar = pessoa
   await client.send_message(message.channel, "Voce tera cancer" + marcar)
   
#
async def what(message):
   await client.send_message(message.channel, "¯\_(ツ)_/¯")

#
async def resposta_teste(message):
   await client.send_message(message.channel, "Iae!")

#
async def info(message):
   await client.send_message(message.channel, "```Bot da pedo bear, links:```")


async def help(message):
   await client.send_message(message.channel, "```Comandos: /time (horario, dia, etc) /spam (message) /say (message) /xingar (author) /clear (numero de mensagens para apagar)```")

async def spam(message):
    i = 1
    spam = message.content.strip("/spam")
    while (i < 8):
       await client.send_message(message.channel, spam)
       i = i + 1
@client.event
async def on_message(message):
    author = message.author

    if author == client.user:
       return # nao responder as propias mensagens

    if message.content.startswith("/test"):
        await resposta_teste(message)
    if message.content.startswith("/info"):
        await info(message)
    if message.content.startswith("?"):
        await what(message)

    if message.content.startswith("/xingar"):
        await xingar(message)

    if message.content.startswith("/help"):
        await help(message)

    if message.content.startswith("/say"):
        await say(message)

    if message.content.startswith("/spam"):
        await spam(message)

    if message.content.startswith("/time"):
        await time(message)

    if message.content.startswith("/quit"):
        await quit(message)
    if message.content.startswith('/clear'):
        clear_chat_channel(message)

@client.event
async def on_ready():
        client.accept_invite("https://discordapp.com/oauth2/authorize?client_id=269166666519281664&scope=bot&permissions=2146958463")



client.run("MjY5MTY2NjY2NTE5MjgxNjY0.C1mCGg.7V_WwlopMvrm2jJ0M8juyd3fDFA")
