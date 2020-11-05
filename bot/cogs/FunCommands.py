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
    async def hing_command(self,ctx,*args,**kwargs):
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

    @commands.command(name="soul")
    async def souling_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 303480386271313921:
            await ctx.send("My fave sister")
        elif ctx.author.id == 268122068007124993 or ctx.author.id == 773319306208608266:
            await ctx.send("Well done, you have tested, and it has worked. Big yay")
        else:
            await ctx.send("You're not Soul... go away")
'''
    @commands.command(name="kay")
    async def ching_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 728658188412649479:
            await ctx.send("Yus, you are the best kay to ever exist. We appreciate you and everything you've done. Thank you for baring with my creator all these years")
        else:
            await ctx.send("To sum it up, Kay is big great")
'''
'''
    @commands.command(name="test")
    async def ing_command(self,ctx,*args,**kwargs):
        #fil = File('img.png',filename="img.png")
        #await ctx.send(content="ping",file=fil)
        fil = File('img.png',filename="img.png")
        await ctx.send(content="ping",file=fil)
'''
def setup(bot):
    bot.add_cog(FunCommands(bot))