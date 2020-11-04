from discord.ext.commands import Cog
from discord.ext import commands
from discord import file

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
        elif ctx.author.id == 759060138006020146:
            await ctx.send("FUS RO REE")
        elif ctx.author.id == 541615594202464257:
            await ctx.send("Joke's on you, I'm into ree... hehehe")
        elif ctx.author.id == 303480386271313921:
            await ctx.send("Ree, y toes are big cold.... poop")
        else:
            await ctx.send("Hello, you have been blessed by the ree.")
'''
    @commands.command(name="test")
    async def ching_command(self,ctx,*args,**kwargs):
        await ctx.send(file('dog.png'))
''' 

    

def setup(bot):
    bot.add_cog(FunCommands(bot))