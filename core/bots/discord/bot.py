import asyncio

import discord

from config import Config
from core.bots.discord.client import client
from core.bots.discord.message import MessageSession, FetchTarget
from core.elements import MsgInfo, Session, Module
from core.loader import Modules
from core.logger import Logger
from core.parser.message import parser
from core.scheduler import Scheduler


@client.event
async def on_ready():
    Logger.info('Logged on as ' + str(client.user))
    gather_list = []
    for x in Modules:
        if isinstance(Modules[x], Module) and Modules[x].autorun:
            gather_list.append(asyncio.ensure_future(Modules[x].function(FetchTarget)))
    await asyncio.gather(*gather_list)
    Scheduler.start()


@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return
    Logger.info(str(message) + message.content)
    target = "DC|Channel"
    if isinstance(message.channel, discord.DMChannel):
        target = "DC|DM|Channel"
    msg = MessageSession(target=MsgInfo(targetId=f"{target}|{message.channel.id}",
                                        senderId=f"DC|Client|{message.author.id}",
                                        senderName=message.author.name, targetFrom=target, senderFrom="DC|Client"),
                         session=Session(message=message, target=message.channel, sender=message.author))
    await parser(msg)


dc_token = Config('dc_token')
if dc_token:
    client.run(dc_token)
