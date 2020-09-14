import discord
from discord.ext import commands

class OwnerCog(commands.Cog):
    """
    Owner-only commands that the owner of the bot can use.

    TODO: Make this cog an administrator - only type cog
    TODO: Make nukeUser and nukeMessages more optimized
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nukeUser', hidden=True)
    @commands.is_owner()
    async def nukeUser(self, ctx, *, arg: str):
        # Preparing for deletion
        message_deleted = 0
        message_iter = 0

        channel = ctx.channel
        init_message = await ctx.send("Number of Deleted Messages: 0")

        # Going through the entire channel
        async for message in channel.history(limit=100000):
            message_iter += 1
            content = message.content
            if int(arg) == message.author.id:

                # Delete message
                await message.delete()
                message_deleted += 1

                # Update progress bar
                update_content = "% Number of Deleted Messages: " + str(message_deleted)
                await init_message.edit(content = update_content)

        # Final progress update
        update_content = "% Number of Deleted Messages: " + str(message_deleted)
        await init_message.edit(content = update_content)

    @commands.command(name='nukeMessages', hidden=True)
    @commands.is_owner()
    async def nukeMessages(self, ctx, *, arg: str):
        # We will not allow messages that are too small
        if len(arg) < 3:
            await ctx.send('Message too small to be nuked')
            return

        # Preparing for deletion
        message_deleted = 0
        message_iter = 0

        channel = ctx.channel
        init_message = await ctx.send("Number of Deleted Messages: 0")

        # Going through the entire channel
        async for message in channel.history(limit=100000):
            message_iter += 1
            content = message.content
            if arg.lower() in content.lower():

                # Delete message
                await message.delete()
                message_deleted += 1

                # Update progress bar
                update_content = "% Number of Deleted Messages: " + str(message_deleted)
                await init_message.edit(content = update_content)

        # Final progress update
        update_content = "% Number of Deleted Messages: " + str(message_deleted)
        await init_message.edit(content = update_content)

def setup(bot):
    bot.add_cog(OwnerCog(bot))
