
from discord.ext import commands, tasks

class PetManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.decreaseHunger.start()
        self.decreaseAffection.start()
        self.decreaseBoredom.start()

    def cog_unload(self):
        self.decreaseHunger.cancel()
        self.decreaseAffection.cancel()
        self.decreaseBoredom.cancel()


    
    def getHungerStatus(self):

    
    @tasks.loop(minutes=8.0)
    async def decreaseHunger(self):
        self.hunger -= 1
        print(self.hunger)

    @tasks.loop(minutes=10.0)
    async def decreaseAffection(self):
        self.love -= 1
        print(self.love)

    @tasks.loop(minutes=12.0)
    async def decreaseBoredom(self):
        self.boredom -= 1
        print(self.boredom)

    @commands.Cog.listener("on_message")
    async def on_message(self, message):   
        if message.author.id == self.bot.user.id:
            return

        if "test" in message.content:
            await message.channel.send("test")
            await message.channel.send(self.getStatus())
    
        if "fat" in message.content.lower():
            await message.channel.send(f"FAT!? WHO SAID IM FAT!? IM NOT FAT!!! \n https://tenor.com/view/mad-mad-cat-angry-cat-cat-cat-meme-gif-6241738800057917520")

        if message.content.lower() == "sfingi laugh at this fool":
            await message.channel.send(f"https://tenor.com/view/orange-cat-laughing-gif-13031147940704744720")
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send("hello")

    @commands.command()
    async def feed(self, ctx):
        #This method allows the discord user to feed Sfingi and add to his hunger and returns a randomized sound
        self.hunger = self.recoverAmt 
        randomThanksText = self.randomizeSound(self.thanksText) 
        randomFullText = self.randomizeSound(self.fedText)
        fullMsg = f'"{randomThanksText}" - {randomFullText}'
        await ctx.send(fullMsg)

    @commands.command()
    async def pet(self, ctx):
        #This method allows the discord user to pet Sfingi and add to his boredom and love and returns a randomized sound.
        self.love += self.recoverAmt / 2
        self.boredom += self.recoverAmt // 3
        sound = self.randomizeSound()
        print(f"Petting sound is {sound}")
        return sound    
    
    @commands.command()
    async def getStatus(self, ctx):
        #Prints out all the information about sfingi
        hungerState = self.getHungerStatus()
        loveState = self.getLoveStatus()
        boredomState = self.getBoredomStatus()

async def setup(bot):
    await bot.add_cog(PetManager(bot))
    
    


