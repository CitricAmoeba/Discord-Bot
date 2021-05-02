import discord
from discord.ext import commands
import random

#Selection of my favourite games 
games = ['Sea of Thieves', 'Dead by Daylight', 'Team Fortress 2', 'Titanfall 2', 'Apex Legends', 'Town of Salem', 'Fall Guys', 'Papers, Please', 'Among Us', 'Prison Architect', 'Overwatch']

#A client is our connection to discord
client = discord.Client()

#Prepares for use of intents
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

    if 'HELLO THERE' in message.content.upper():
        print('Sending message')
        await message.channel.send('General Kenobi')
        
    elif 'WHAT GAME SHOULD I PLAY?' in message.content.upper():
        print('Sending message')
        await message.channel.send(random.choice(games))
        

#Responds to someone joining a server
@client.event
async def on_member_join(member):
    print('New member recognised')
    channel_id = client.get_channel()   #The ID for the channel to send the message to should be passed in here
    await channel_id.send('Hello ' + member.name + '!')


#Responds to someone leaving a server
@client.event
async def on_member_remove(member):
    print(member.name + ' has left')
    channel_id = client.get_channel() #The ID for the channel to send the message to should be passed in here
    await channel_id.send(member.name + 'has left :(')
    
#Bot announces 
@client.event
async def on_guild_join(guild):
    print('Joined a new guild')
    channel_id = client.get_channel() #The ID for the channel to send the message to should be passed in here
    await channel_id.send("Hey everyone, I'm CitricAmoebot! I'm just a funny, friendly personality created by CitricAmoeba, and I'm happy to be here and interact with you all!")

#I've taken my bot token out for security reasons, but this will need a bot token to work
client.run('')
