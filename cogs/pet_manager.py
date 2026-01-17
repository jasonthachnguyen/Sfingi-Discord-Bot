from sfingi import Sfingi
from discord.ext import commands, tasks

class PetManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sfingi = Sfingi()
        self.decreaseHunger.start()
        self.decreaseAffection.start()
        self.decreaseHygiene.start()

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
    @commands.command()
    async def feed(self, ctx, help="Hello??"):
        """
        Resets the hunger value back to 100 and generates text for user feedback
        """
        self.sfingi.resetHunger()
        randomThanksText = self.sfingi.getThanksText()
        afterFeedText = self.sfingi.getAfterFeedText()
        response = f'"{randomThanksText}" - {afterFeedText}'
        await ctx.send(response)

    @commands.command()
    async def pet(self, ctx):
        """
        Resets the affection back to 100 and generates text for user feedback
        """
        self.sfingi.resetAffection()
        thanksText = self.sfingi.getThanksText()
        afterPetText = self.sfingi.getAfterPetText()
        response = f'"{thanksText}" - {afterPetText}'
        await ctx.send(response)

    @commands.command()
    async def wash(self, ctx):
        """
        Resets the hyigene back to 100 and generates text for user feedback.
        
        :param self: Description
        :param ctx: Description
        """
        self.sfingi.resetHygiene()
        thanksText = self.sfingi.getThanksText()
        afterWashText = self.sfingi.getAfterWashText()
        response = f'"{thanksText}" - {afterWashText}'
        await ctx.send(response)
    
    @commands.command()
    async def status(self, ctx):
        statusMsg = self.sfingi.getStatus()
        await ctx.send(statusMsg)

async def setup(bot):
    await bot.add_cog(PetManager(bot))
    
    


