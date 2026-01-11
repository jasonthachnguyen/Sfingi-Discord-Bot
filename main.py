import discord
from catTracker import catTracker
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os 
import time

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
sfingi = catTracker()

@bot.event
async def on_ready():
    print("Bot is online and ready.")
    print(f"Current hunger, love and boredom levels are {sfingi.getStatus()}")

@bot.event
async def on_member_join(member):
    await member.send(f"dude what's up {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "fat" in message.content.lower():
        await message.channel.send(f"FAT!? WHO SAID IM FAT!? IM NOT FAT!!! \n https://tenor.com/view/mad-mad-cat-angry-cat-cat-cat-meme-gif-6241738800057917520")

    if message.content.lower() == "sfingi meme his ass":
         await message.channel.send(f"https://tenor.com/view/pov-baby-kaiif-kaiif-cat-fat-gif-8082934790615986582")

    if message.content.lower() == "sfingi laugh at this fool":
         await message.channel.send(f"https://tenor.com/view/orange-cat-laughing-gif-13031147940704744720")
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"meow {ctx.author.mention}")

@bot.command()
async def status(ctx):
     await ctx.send(sfingi.getStatus())

@bot.command()
async def pet(ctx):
     await ctx.send(sfingi.pet())

@bot.command()
async def feed(ctx):
    await ctx.send("Feeding...")
    time.sleep(2)
    await ctx.send(sfingi.feed())
    

bot.run(token, log_handler=handler, log_level=logging.DEBUG)