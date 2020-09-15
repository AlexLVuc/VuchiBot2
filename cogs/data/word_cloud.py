import discord
import os

from discord.ext import commands
from os import path
from wordcloud import WordCloud

class WordCloudCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='simpleWordCloud')
    async def simpleWordCloud(self, ctx, *, arg: str):
        """
        Send a simple wordcloud of a user's messages in a channel.
        """
        user_text = ""
        d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

        async for message in ctx.channel.history(limit=100000):
            if int(arg) == message.author.id:
                user_text += message.content + " "

        wordcloud = WordCloud().generate(user_text)
        wordcloud.to_file(path.join(d, f'{arg}.png'))
        filename = path.join(d, f'{arg}.png')
        with open(filename, 'rb') as f:
            await ctx.channel.send(file=discord.File(f, filename))

def setup(bot):
    bot.add_cog(WordCloudCog(bot))
