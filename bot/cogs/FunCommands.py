from discord.ext.commands import Cog
from discord.ext import commands
from discord import File

class FunCommands(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="pong")
    async def ching_command(self,ctx,*args,**kwargs):
        await ctx.send("Haha,FOOLED AGAIN MUHAHAHA")

    @commands.command(name="ree")
    async def ching_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 268122068007124993:
            await ctx.send("Hello ree master, my creator")
        else:
            await ctx.send("Hello, you have been blessed by the ree")

    @commands.command(name="test")
    async def ching_command(self,ctx,*args,**kwargs):
        img = File('dog.png')
        await ctx.send(img)
    

    

def setup(bot):
    bot.add_cog(FunCommands(bot))