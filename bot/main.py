from discord.ext.commands import Bot
from discord.errors import LoginFailure
from discord import __version__, Intents
from os import listdir,getenv,chdir
from os.path import dirname,abspath,join

BASE_DIR = dirname(dirname(abspath(__file__)))
COG_DIR = join(BASE_DIR,join("bot","cogs"))
TOKEN = getenv("DISCORD_TOKEN","69")


description = """A Fully Custom Discord Bot"""
command_prefix = ("__",)

bot = Bot(command_prefix=command_prefix,description=description,intents=Intents.all())

print ("Discord Version:",__version__)
print ("Loading Bot, Please Wait")

@bot.event
async def on_ready():
    print("Bot has loaded")
    print("Version: "+__version__)
    print(f'Name {str(bot.user)}')
    print(f"ID: {bot.user.id}")
@bot.event
async def on_message(message):
    if(message.author.bot): return
    if('\U0001F440' in message.content):
        await message.add_reaction('\U0001F440')

    await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx,*args,**kwargs):
    await ctx.send(content='Pinging')

cogs = sorted(listdir(COG_DIR))
for cog in cogs:
      if cog.endswith(".py"):
         try:
            cog = f"cogs.{cog.replace('.py','')}"
            bot.load_extension(cog)
            print(f"loaded {cog}")
         except Exception as e:
            print(f"{cog} can not be loaded")
            print(e)


try:
    bot.run(TOKEN,bot=True,reconnect=True)
except LoginFailure as e:
    print(f'Bot Failed to Login this is most likely because of Invalid Token given.')
except Exception as e:
    print(f"Major Bot Error - {type(e)}")
    print(e)