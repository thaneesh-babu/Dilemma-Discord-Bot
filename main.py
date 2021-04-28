'''
Commands: coinflip, trueorfalse, person 1 or person 2 to break arguments, matcher - compatibility
of two ppl, random name generator, probability generator, 
 '''

import discord
from discord.ext import commands
import random
from match import matchingAlgo

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.help'))
    print('Bot is up and running')

@client.event
async def on_message(message):
    
    if message.content.startswith('.match'):
        matching_percent = matchingAlgo(message.content)

        await message.channel.send("Compatibility of entered names: {}".format(matching_percent))
    
    if message.content.startswith('.coinflip'):
        await message.channel.send(random.choice(['Head','Tail']))
    
    if message.content.startswith('.rolldice'):
        await message.channel.send(random.choice([1,2,3,4,5,6]))
    
    if message.content.startswith('.yesorno'):
        await message.channel.send(random.choice(['Yes','No']))
    
    if message.content.startswith('.trueorfalse'):
        await message.channel.send(random.choice(['True','False']))
    
    if message.content.startswith('.chanceit'):
        await message.channel.send('There is a {}% probability of that happening'.format(str(round(random.uniform(0,100), 2))))

    if message.content.startswith('.help'):
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
        embed.add_field(name='.match <name1>, <name2>', value='Returns compatibility of two names', inline=False)
        embed.add_field(name='.help', value='Displays this message', inline=False)

        await message.channel.send(embed=embed)






client.run('ODM2Mjk5ODQ1OTg3NTk4MzU2.YIb-7A.OiU5NGfcSl6-ad7C8K8yeYMv298')