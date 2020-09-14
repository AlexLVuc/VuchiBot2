import discord
from discord.ext import commands
import sys, traceback

@bot.event
async def on_ready():
    print(f'\nBot Ready: {bot.user.name} - {bot.user.id} \n Version: {discord.__version__}\n')
    await bot.change_presence(game=discord.Game(name='Watching a king', type=1, url='https://www.twitch.tv/kooobie'))
    print(f'Successfully booted')
