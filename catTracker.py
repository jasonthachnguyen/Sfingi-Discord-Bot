import random 
import time
from discord.ext import tasks, commands

class catTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hunger = 100
        self.boredom = 100
        self.love = 100
        self.grooming = 100
        self.recoverAmt = 100
        self.fedText = [
            "Sfingi is feeling nice and full!",
            "Even though his belly is ready to burst, he wants more food...",
            "Sfingi looks up at you with his fat little belly.",
            "Sfingi walks away with his belly bouncing around."
        ]
        self.thanksText = ["thanks big dawg, ppreciate it", "merow", "meoww", "purr", "grrr", "meYOEW"]

    # def cog_unload(self):
    #     self.decreaseHunger.cancel()

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        
        if "test" in msg:
            await msg.channel.send("test")

    # @tasks.loop(seconds=5.0)
    # async def decreaseHunger(self):
    #     self.hunger -= 1
    #     print(self.hunger)

    # @decreaseHunger.before_loop
    # async def before_decrease(self):
    #     print("Waiting...")
    #     await self.bot.wait_until_ready()

    def getStatus(self):
        #Prints out all the information about sfingi
        return f"Sfingi's current stats - hunger: {self.hunger}, boredom: {self.boredom}, love: {self.love}"

    def feed(self):
        #This method allows the discord user to feed Sfingi and add to his hunger and returns a randomized sound
        self.hunger = self.recoverAmt 
        randomThanksText = self.randomizeSound(self.thanksText) 
        randomFullText =self.randomizeSound(self.fedText)
        return f'"{randomThanksText}" - "{randomFullText}"'
    
    def pet(self):
        #This method allows the discord user to pet Sfingi and add to his boredom and love and returns a randomized sound.
        self.love += self.recoverAmt / 2
        self.boredom += self.recoverAmt // 3
        sound = self.randomizeSound()
        print(f"Petting sound is {sound}")
        return sound
    
    def randomizeSound(self, textList):
        #Returns a randomized sound when a list of sounds
        sound = textList[random.randrange(len(textList))]
        return sound
    
    
    


