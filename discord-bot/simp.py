import random
import discord
import os
from dotenv import load_dotenv


client = discord.Client()

bkwonUserId = 182676713212346368
risenUserId = 192417297061642240
bZhangUserId = 171533692127150080
shrekUserId = 161332364574851072
load_dotenv()

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
    # if message.author == client.user:
    #     return

    if (message.author.id == bkwonUserId or message.author.id == risenUserId or message.author.id == bZhangUserId or message.author.id == shrekUserId):
        randomInt = random.randint(0, len(simpQuotes)  -  1)
        print(message.author)
        await message.channel.send(message.author.name + ", " + simpQuotes[randomInt])

client.run(os.getenv('TOKEN'))