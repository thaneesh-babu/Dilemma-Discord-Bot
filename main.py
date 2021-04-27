'''
Create a help function where all possible commands are listed
Commands: coinflip, trueorfalse, person 1 or person 2 to break arguments, matcher - compatibility
of two ppl, random name generator, probability generator, 
 '''

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
help_msg = "``` DILEMMA HELP CENTER \n\n 1. .chanceit <event> - returns the probability of said event happening \n 2. .coinflip - returns the outcome of a coin flip \n 3. .rolldice - returns the outcome of rolling a dice \n 4. .trueorfalse <statement> - returns whether the said statement is true or false \n 5. .yesorno <question> - answers yes or no to said question \n 6. .delete <amount> - clears entered amount of messages in the channel \n 7. .help - shows this message```"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.help'))
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

@client.command()
async def help(ctx):
    await ctx.send(help_msg)




client.run('ODM2Mjk5ODQ1OTg3NTk4MzU2.YIb-7A.OiU5NGfcSl6-ad7C8K8yeYMv298')