#bot discord
#criado por Mr Monkey
import asyncio
import aiohttp
import logging, traceback
import sys, re, io, enum
import tempfile, os, hashlib
import itertools
import datetime
from collections import namedtuple
from os.path import split as path_split
from time import ctime
import discord
client = discord.Client()

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

@asyncio.coroutine


async def clear(message):
  deletar = message.content.strip("/clear")
  deletarint = int(deletar)
  await client.purge_from(message.channel, limit=deletarint)
  await client.send_message(message.channel, "🗑️ |``Eu deletei " + deletar + " mensagens``")
async def quit(message):
  await client.send_message(message.channel, "QUER MESMO SAIR ?(y/n)")

async def time(message):
  time = ctime()
  await client.send_message(message.channel, "⏰ " + time)
#
async def say(message):
   say = message.content.strip("/say")
   await client.send_message(message.channel, say)

async def radio():
    #aqui o bot entra no canal logo quando o bot entra no servidor.
    #await client.send_message(message.channel, "bot entrou no canal de audio")

    canal_voz = discord.Object(id='12324234183172')#canal de voz em que o bot entra.(ID)
    await client.join_voice_channel(canal_voz)

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

async def info(message):
   await client.send_message(message.channel, "```Bot da pedo bear, links:```")


async def help(message):
   await client.send_message(message.channel,
   """
   ```Comandos:
   /time (horario, dia, etc)
   /spam (message)
   /say (message)
   /xingar (author)
   /clear (numero de mensagens para apagar)```
   """)


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
        await clear(message)


@client.event
async def on_ready():
        await client.change_presence(game=discord.Game(name="/help para ajuda"))
        radio()
        client.accept_invite("https://discordapp.com/oauth2/authorize?client_id=269166666519281664&scope=bot&permissions=2146958463")
        client.run("your token here")
