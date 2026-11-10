import discord
from discord import app_commands
from discord.ext import commands, tasks
from sfingi import Sfingi

# PetManager inherits from Cog
# name adds metadata to the Cog
class PetManager(commands.Cog, name="Pet Manager"):
    def __init__(self, bot):
        self.bot = bot
        self.sfingi = Sfingi()

    def cog_unload(self):
        self.decreaseHunger.cancel()
        self.decreaseAffection.cancel()
        self.decreaseHygiene.cancel()

    @tasks.loop(seconds=2.0)
    async def decreaseHunger(self):
        self.sfingi.decreaseHunger()
        print(self.sfingi.getHungerValue())

    @tasks.loop(seconds=2.0)
    async def decreaseAffection(self):
        self.sfingi.decreaseAffection()
        print(self.sfingi.getAffectionValue())

    @tasks.loop(seconds=2.0)
    async def decreaseHygiene(self):
        self.sfingi.decreaseHygiene()
        print(self.sfingi.getHygieneValue())

    # @commands.Cog.listener("on_ready")
    # async def on_ready(self):
        # self.decreaseHunger.start()
        # self.decreaseAffection.start()
        # self.decreaseHygiene.start()

    #EVENTS
    @commands.Cog.listener("on_message")
    async def on_message(self, message):   
        if message.author.id == self.bot.user.id:
            return
    
        if "fat" in message.content.lower():
            await message.channel.send(f"FAT!? WHO SAID IM FAT!? IM NOT FAT!!! \n https://tenor.com/view/mad-mad-cat-angry-cat-cat-cat-meme-gif-6241738800057917520")

        if message.content.lower() == "sfingi laugh at this fool":
            await message.channel.send(f"https://tenor.com/view/orange-cat-laughing-gif-13031147940704744720")

    #COMMANDS    

    # Declaring a slash command using the app_commands.command decorator from the discord module
    @app_commands.command()
    async def feed(self, interact):
        """
        Feeds Sfingi some food and fill up his belly!
        """
        self.sfingi.resetHunger()
        randomThanksText = self.sfingi.getThanksText()
        afterFeedText = self.sfingi.getAfterFeedText()
        response = f'"{randomThanksText}" - {afterFeedText}'
        await interact.response.send_message(response)

    @app_commands.command()
    async def pet(self, interact):
        """
        Pet Sfingi so that he feels loved.
        """
        self.sfingi.resetAffection()
        thanksText = self.sfingi.getThanksText()
        afterPetText = self.sfingi.getAfterPetText()
        response = f'"{thanksText}" - {afterPetText}'
        await interact.response.send_message(response)

    @app_commands.command()
    async def wash(self, interact):
        """
        Wash the stink out of Sfingi!
        """
        self.sfingi.resetHygiene()
        thanksText = self.sfingi.getThanksText()
        afterWashText = self.sfingi.getAfterWashText()
        response = f'"{thanksText}" - {afterWashText}'
        await interact.response.send_message(response)
    
    @app_commands.command()
    async def status(self, interact):
        """
        Get the status on how Sfingi is doing.
        """
        statusMsg = self.sfingi.getStatus()
        await interact.response.send_message(statusMsg)

    @app_commands.command()
    async def testcog(self, interact):
        """
        Get the status on how Sfingi is doing.
        """
        await interact.response.send_message("cog works too")

# Main entry point when main.py loads this extension 
async def setup(bot):
    await bot.add_cog(PetManager(bot))
    
    


