from discord.ext.commands import Cog
from discord.ext import commands

class FunCommands(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ching_command(self,ctx,*args,**kwargs):
        await ctx.send("Haha,FOOLED AGAIN MUHAHAHA")
    

    

def setup(bot):
    bot.add_cog(FunCommands(bot))