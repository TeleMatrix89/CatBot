from discord.ext.commands import Cog
from discord.ext import commands
from discord import Member, Embed, Colour, User
from discord.ext.commands import Cog,BucketType
from discord import File

class FunCommands(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="pong")
    async def pong_command(self,ctx,*args,**kwargs):
        await ctx.send("Haha,FOOLED AGAIN MUHAHAHA")

    @commands.command(name="ree")
    async def ree_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 268122068007124993:
            await ctx.send("Hello ree master, my creator")
        else:
            await ctx.send("Hello, you have been blessed by the ree.")

    @commands.command(name="dog")
    @commands.cooldown(rate=3, per=10, type=BucketType.member)
    @commands.MaxCurrency(3, BucketType.member, wait = True)
    async def dog_command(self,ctx,*args,**kwargs):
        fil = File('img.png',filename="img.png")
        if ctx.author.id == 583260078157594624:
            await ctx.send("no spam pls")
        else:
            await ctx.send(content="Have doggo",file=fil)

    @get_member_info.error
    async def get_member_error(self,ctx,error):
        if(isinstance(error,commands.CommandOnCooldown)):
            return await ctx.send(f"Slow down {ctx.author} and retry after {int(error.retry_after)} seconds")
        await ctx.send("Command Errored")

def setup(bot):
    bot.add_cog(FunCommands(bot))