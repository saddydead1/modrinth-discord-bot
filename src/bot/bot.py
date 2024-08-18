import discord
import os 
import asyncio
from discord import app_commands
from discord.ext import commands
import logging
import time
import threading
from httpmod.client import Modrinth
from models.Version import Version


TOKEN = os.environ.get('TOKEN')
CHAT_ID = int(os.environ.get('CHANNEL_ID'))

log = logging.getLogger(__name__)
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

async def update():
    while True:
        r = await Modrinth.request()
        await send(r)
        time.sleep(60)

class Bot:
    @staticmethod
    def init() -> None:
        log.info('bot is starting')
        bot.run(TOKEN)


    @bot.event
    async def on_ready() -> None:
        log.info('bot started')
        await bot.wait_until_ready()
        global chat
        chat = bot.get_channel(CHAT_ID)
        await bot.change_presence(status = discord.Status.online, activity=discord.Game(name='Minecraft'))

        await Modrinth.update()

        bot.loop.create_task(update())

        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)


async def send(text: Version | None) -> None:
    if (text == None):
        return
    else:
        await chat.send(f'''
New Version! @everyone
                        
Name - {text.name}
Version - {text.version}
Name - {text.version_type}
Changelog - {text.changelog}
            ''')



    

