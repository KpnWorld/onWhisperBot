import discord
from discord.ext import commands
import os
import random
import asyncio
import time
import datetime
import json
import aiohttp
import logging
import traceback
import sys

# Set up the logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Set up the bot
bot = commands.Bot(command_prefix='!', description='A bot that greets the user back.')
bot.remove_command('help')

# Load the cogs
if __name__ == '__main__':
    for extension in os.listdir('cogs'):
        if extension.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{extension[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
                