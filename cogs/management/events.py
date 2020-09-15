import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Upon connecting to a server, the bot will print out some log messages for
        server owners to reference as well as changing the presence of the bot.
        """
        print(f'\nBot Ready: {self.bot.user.name} - {self.bot.user.id} \n Version: {discord.__version__}\n')
        await self.bot.change_presence(activity=discord.Streaming(name='Watching a king', type=1, url='https://www.twitch.tv/kooobie'))
        print(f'Successfully booted')

    @commands.Cog.listener()
    async def on_disconnect(self, message):
        """
        Upon disconnecting to a server, the bot will remove any png images created
        by the 'data' cog.

        TODO: Make an option to save these images in a meaningful way
        """
        print(f'\nBot disconnected: {self.bot.user.name} - {self.bot.user.id} \n Version: {discord.__version__}\n')
        directory = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        pathlist = directory.glob('*.png')
        for path in pathlist:
             path.unlink()
        print(f'Successfully disconnected')

def setup(bot):
    bot.add_cog(Events(bot))
