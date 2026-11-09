import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os 
import pathlib

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = True

description = "A Sfingi bot."

# This class holds the logic for the main manager component
class Manager(commands.Bot):
    async def on_ready(self):
        print("Bot is online and ready.")

    #setup_hook will only run once before the bot starts running
    async def setup_hook(self):
        # Use pathlib.Path to look into directory "cogs" and search for any file that ends with .py
        for file in pathlib.Path("cogs").rglob("*.py"):
            # If the name of file starts with _, then it's private skip it
            if file.stem.startswith("_"):
                continue
            # Change the suffix of the file to nothing, separate the path into its parts and join each part with a period
            # This formats it properly so that discord.py can load the extension
            await self.load_extension(".".join(file.with_suffix("").parts))
            print(f"Loaded {file}")

manager = Manager(command_prefix=commands.when_mentioned_or("!"), description=description, intents=intents, help_command=None)

# Define a command for manager that lets the user reload an extension by using the !reload command and extension name
@manager.command()
async def reload(ctx: commands.Context, extension: str):
    await manager.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}")

manager.run(token)
