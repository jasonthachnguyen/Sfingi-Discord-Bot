import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import pathlib

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = True


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


manager = Manager(command_prefix=commands.when_mentioned_or("!"), description="A Sfingi bot.", intents=intents, help_command=None)

manager.run(token)
