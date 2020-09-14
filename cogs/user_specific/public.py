import discord
from discord.ext import commands

class PublicCog(commands.Cog):
    """ A cog for commands that any member in a guild ( server ) can use."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hellobot')
    async def hellobot(self, ctx):
        """Hello World!"""
        await ctx.send('Hello! :)')

# In loading a cog, we refer to the file name
def setup(bot):
    bot.add_cog(PublicCog(bot))
