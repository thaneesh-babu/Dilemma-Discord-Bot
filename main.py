'''
Commands: coinflip, trueorfalse, person 1 or person 2 to break arguments, matcher - compatibility
of two ppl, random name generator, probability generator, 
 '''

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

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
    embed = discord.Embed(
        colour = discord.Colour.gold()
    )

    embed.set_footer(text="For more information, contact the bot's creator: BinaryBorder#0015")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/836241107779452948/836550937731661854/dilemmabotpfp.png")
    embed.set_author(name="DILEMMA BOT HELP CENTER")
    embed.add_field(name='.chanceit <event>', value='Returns the probability of said event happening', inline=False)
    embed.add_field(name='.coinflip', value='Returns the outcome of flipping a coin', inline=False)
    embed.add_field(name='.rolldice', value='Returns the outcome of rolling a dice', inline=False)
    embed.add_field(name='.trueorfalse <statement>', value='Returns whether the said statement is true or false', inline=False)
    embed.add_field(name='.yesorno <question>', value='Answers yes or no to said question', inline=False)
    embed.add_field(name='.delete <amount>', value='Clears entered amount of messages in the channel', inline=False)
    embed.add_field(name='.help', value='Displays this message', inline=False)

    await ctx.send(embed=embed)



client.run('ODM2Mjk5ODQ1OTg3NTk4MzU2.YIb-7A.OiU5NGfcSl6-ad7C8K8yeYMv298')