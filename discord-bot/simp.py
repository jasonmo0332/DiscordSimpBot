
import random
import discord
import os


client = discord.Client()

bkwonUserId = 182676713212346368
risenUserId = 192417297061642240
bZhangUserId = 171533692127150080

simpQuotes = ["Shut up simp", "Sorry no simps allowed", 
                "Did she even read your name on stream?", 
                "Lol have you even seen her nudes?", 
                "Bro, you know she's a dude right?", 
                "Hey wanna play League? Just kidding I have a boyfriend already", 
                    "UwU, you gay"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    if (message.author.id == bkwonUserId or message.author.id == risenUserId or message.author.id == bZhangUserId):
        randomInt = random.randint(0, len(simpQuotes)  -  1)
        
        await message.channel.send(simpQuotes[randomInt])

client.run(os.getenv('TOKEN'))