# import Discord Package
import discord
from discord.ext import commands
import pandas as pd 


#Client (our bot)
client = commands.Bot(command_prefix = "--")

#Code :)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('MineCraft'))

    df = pd.DataFramew


@client.command(name='about')
async def about(context):

    myembed = discord.Embed(title="About me" , description="I am a bot made by Tirth Z and a  helper bot for this server", color=0xFD8900)
    myembed.add_field(name="My Name :",value="Good Boy",inline=False )
    myembed.add_field(name="Born on", value="04-03-2021",inline=False)
    myembed.add_field(name="Work" , value="To help you :)",inline=False)
    myembed.set_footer(text="This is all about me :-)")
    myembed.set_author(name="Tirth Z")
    
    await context.message.channel.send(embed=myembed)

@client.command(name='server')
async def server(context):
        myserv = discord.Embed(title="Server" , color=0xFD8900)
        myserv.add_field(name=" Name ",value="Mcplayers2020",inline=False )
        myserv.add_field(name="Started on", value="04-03-2021",inline=False)
        myserv.add_field(name="IP :" , value="mcplayers2021.aternos.me",inline=False)
        myserv.set_footer(text="Have a Nice day :)")

        await context.message.channel.send(embed=myserv)

@client.event
async def on_message(message):

    if message.content == 'Hi':
        gchannel = client.get_channel(788344641195606059)
        await gchannel.send("Hola !!")
     
    if message.content == 'send a dm':
        await message.author.send('This is a DM, Have A Good Day !')

    await client.process_commands(message)

#Run a client on a server 
client.run('ODE3MDQ0MDYzMzM3MTg1MzAw.YEDxlA.eHn1-I3M_I2t97kGNg-KLVgJ2EY')
