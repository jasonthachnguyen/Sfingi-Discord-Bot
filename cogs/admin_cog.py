import discord
from discord import app_commands
from discord.ext import commands
class AdminCog(commands.Cog):
    """
    A cog that holds tasks and commands for adminstrative purposes or server management - not for regular users. 
    """
    def __init__(self, bot):
        self.bot = bot
    
    # COMMANDS

    # Define a command for manager that lets the user reload an extension by using the !reload command and extension name
    @app_commands.command(description="Reload an extension by passing the extension name")
    async def reload(self, interact: discord.Interaction, extension: str):
        await self.bot.reload_extension(f"cogs.{extension}")
        await interact.response.send_message(f"Reloaded {extension}")
        
    # Define a command that lets the owner of the server sync all commands globally 
    # NOTE: Probably going to be changed once I learn more about command syncing
    @commands.command(description="Sync all commands to the current guild")
    @commands.is_owner()
    async def sync(self, ctx: commands.Context):
        # Try catch block that uses the provided id for server
        try:
            # Sync returns a list of all commands that were synced
            synced = await self.bot.tree.sync()
            # Can check the number of commands that were successfully synced
            await ctx.send(f"Synced {len(synced)} commands to {ctx.guild}")
            
        except Exception as e:
            print(f"Error syncing commands: {e}")
            
async def setup(bot):
    await bot.add_cog(AdminCog(bot))
