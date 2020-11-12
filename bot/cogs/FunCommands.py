from discord.ext.commands import Cog
from discord.ext import commands
from discord import Member, Embed, Colour, User
from discord.ext.commands import BucketType
from discord import File
from datetime import datetime

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
    async def dog_command(self,ctx,*args,**kwargs):
        fil = File('img.png',filename="img.png")
        if ctx.author.id == 583260078157594624:
            await ctx.send("no spam pls")
        else:
            await ctx.send(content="Have doggo",file=fil)

    @commands.command(name="member")
    async def get_member_info(self, ctx, mentioned:Member=None,*args):
        if (ctx.guild is None): return ctx.send("You are not in a guild")
        member:Member = mentioned if mentioned else ctx.author
        emb = Embed(colour=Colour.red(), timestamp=datetime.now())
        emb.set_author(name=f"{member}", icon_url=member.avatar_url)

        emb.add_field(name="Top-Role",value=f"Name: {member.top_role}\n\
            Colour: {member.top_role.colour}\n\
            No. of people with Role: {len(member.top_role.members)}\n\
            CreatedAt: {member.top_role.created_at}")
        emb.add_field(name="info",value=f"JoinDate: {member.joined_at}\n\
            Nick: {member.nick}\n\
            CreatedAt: {member.created_at}")
        emb.set_footer(text=f"{member.id}")
        await ctx.send(embed=emb) 


def setup(bot):
    bot.add_cog(FunCommands(bot))