import discord
from discord.ext import commands
import sys, traceback

# Initial imports, reference cogs like cog.file
# If we have commands.py with some cog CommandsCog, we reference it as:
# cogs.commands
cogs = [
        'cogs.user_specific.public',
        'cogs.management.load',
        'cogs.user_specific.owner'
       ]

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
    prefixes = ['>>', '`']
    return commands.when_mentioned_or(*prefixes)(bot, message)

if __name__ == '__main__':
    bot = commands.Bot(command_prefix=get_prefix, description='Utility bot')
    for cog in cogs:
        bot.load_extension(cog)
    token = input('ENTER BOT TOKEN: \n')
    bot.run(token, bot=True, reconnect=True)
