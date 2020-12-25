import discord
from discord.ext import commands
import random

#Selection of games 
games = ['Sea of Thieves', 'Dead by Daylight', 'Team Fortress 2', 'Titanfall 2', 'Apex Legends', 'Town of Salem', 'Fall Guys', 'Papers, Please', 'Among Us', 'Prison Architect']

#A client is our connection to discord
client = discord.Client()

#Prepares for use of intents, these are needed so we can welcome new members to the guild
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix ='!', intents = intents)


#Called when the bot joins a guild
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#Responds appropriately to messages based on the input
@client.event
async def on_message(message):
    #Prevents the bot from responding to it's own messages
    if message.author == client.user:
        return

    if message.content == 'Hello there':
        print('Kenobi')
        await message.channel.send('General Kenobi')
        
    elif message.content == 'What game should I play?':
        await message.channel.send(random.choice(games))
        

#Responds to someone joining a server
@client.event
async def on_member_join(member):
    print('New member recognised')
    channel_id = client.get_channel(784881512230813716)
    await channel_id.send('Hello ' + member.name+'!')
    
#Add the bot's token in here as a string format
client.run('')
