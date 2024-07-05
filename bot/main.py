import discord, os
from discord.ext.commands import Bot
from tools.startup import StartUp


# install discord.py, and os


# Name the class
class Moon(Bot):
    def __init__(self):
        # Put your id in owner_ids and choose ur prefix
        super().__init__(command_prefix="!!", allowed_mentions=discord.AllowedMentions(roles=False, everyone=False, users=True, replied_user=False), intents=discord.Intents.all(), owner_ids=[465895574172860437])
        # Put ur color here for embeds
        self.color = "#E6E6FA"
        # Put emojis these are gonna be needed for later 
        self.yes = ":thumbsup:"
        self.no = ":thumbsdown:"

    # This is where you start the bot
    async def setup_hook(self):
        print("Trying to start the bot...")
        await self.load_extension('jishaku')
        await StartUp.loadcogs(self)
        print(f"Connected to Discord API as {self.user}")


# Change the name if u changed the class name
bot = Moon()

if __name__ == '__main__':
  bot.run("TOKEN", reconnect=True)
