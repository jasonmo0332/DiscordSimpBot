import random
import discord
import os
from dotenv import load_dotenv


client = discord.Client()

#Constants of user Ids as constants
bkwonUserId = 182676713212346368
risenUserId = 192417297061642240
bZhangUserId = 171533692127150080
shrekUserId = 161332364574851072

#Loads the .env file for the discord bot's token
load_dotenv()

#List of quotes for our bot to pick from randomly
simpQuotes = ["shut up simp", "sorry no simps allowed", 
                "did she even read your name on stream?", 
                "Lol have you even seen her nudes?", 
                "bro, you know she's a dude right?", 
                "hey wanna play League? Just kidding I have a boyfriend already", 
                    "UwU, you gay"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):


    if (message.author.id == bkwonUserId):
        randomInt = random.randint(0, len(simpQuotes)  -  1)
        await message.channel.send(message.author.name + ", " + simpQuotes[randomInt])

client.run(os.getenv('TOKEN'))