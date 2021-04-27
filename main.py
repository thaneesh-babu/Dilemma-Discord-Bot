'''
Create a help function where all possible commands are listed
Commands: coinflip, trueorfalse, person 1 or person 2 to break arguments, matcher - compatibility
of two ppl, random name generator, probability generator, 
 '''

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.<command>'))
    print('Bot is up and running')

@client.command()
async def coinflip(ctx):
    await ctx.send(random.choice(['Head','Tail']))

@client.command()
async def rolldice(ctx):
    await ctx.send(random.choice([1,2,3,4,5,6]))

@client.command()
async def yesorno(ctx):
    await ctx.send(random.choice(['Yes','No']))

@client.command()
async def trueorfalse(ctx):
    await ctx.send(random.choice(['True','False']))

@client.command()
async def chanceit(ctx):
    await ctx.send('There is a {}% probability of that happening'.format(str(round(random.uniform(0,100), 2))))

@client.command()
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=amount)






client.run('ODM2Mjk5ODQ1OTg3NTk4MzU2.YIb-7A.OiU5NGfcSl6-ad7C8K8yeYMv298')