from disnake import *
from disnake.ext import commands
from assets import functions as func
import traceback
from cogs.points_commands import PointsCommands
import discord

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def help(self,ctx):
        e = Embed(title=":notepad_spiral: Help Menu :notepad_spiral:", description=" ", color=ctx.author.color)
        e.add_field(name="Commands", value="• `/eco points <username>` View how much Capitalist Rubbish you or someone has.\n• `/eco points add <username> <number>` Supply Capitalist Rubbish to any member.*\n• `/eco points remove <member> <number>` Remove Capitalist Rubbish from any member.* \n• `/eco leaderboard` See ranking of all members.\n• `/eco shop`: Shows the shop\n• `/eco shop add <price> <item-name>`: Add a item in the shop.*\n• `/eco shop remove`: Remove a item from the shop.*\n• `/eco shop buy <item-name/item-number>`: Buy a item from the shop.\n*: These commands are only available for use by the minister ")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
