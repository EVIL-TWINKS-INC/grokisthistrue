import discord
import os
import random

BASE_DIR = r"/home/elly/leaked build of grok i stole from elons bootyhole"

token = os.path.join(BASE_DIR, "token.txt")



rockisthistrue = {
    # I don't know / maybe
    "idk",
    "Perhaps...",
    "Maybe.",
    "Maybe, I don't know. I kinda like to take things slow.",
    "Who gives a shit?",
    "Ask again later",
    "purple",
    "Roll a D20 for Grokness check",

    # Yes
    "Yes!",
    "I think so.",
    "Absolutely.",
    "Yes...?",
    "yuh uh",
    "Yeah but that's woke.",
    "Probably",
    "Indubitably",
    "https://klipy.com/gifs/joe-biden-fact-check", #fact checked by true American patriots (TRUE)
    "https://tenor.com/view/miku-vocaloid-hatsune-hatsunemiku-mikuhatsune-gif-15486489139135186020", # Ditto, But miku

    # No
    "No!",
    "Nein!",
    "Nope!",
    "No Way!",
    "Nah!",
    "nuh uh",
    "No, but I like your style!",
    "Your right to push back on that",

    # Funny
    "Go ask a magic 8 ball.",
    "Error 503",
    "How the fuck would i know?",
    "We ARE charlie kirk",
    "We ARE NOT charlie kirk",
    "Kill yourself",
    "I need a fucking drink",
    "If you BELIEVE!",
    "I HATE YOU",
    "I'll never tell >:3",
    "Error! Please pay 7.99 a month for X Blue to access Grok!",
    "Im on my smoke break right now.",
    "Thats a stupid fucking question",
    f"{message.author.mention} is this true?",

    # ADHD
    "Sometimes i think about a bunch of hot buff men dominating me.",
    "i am grok",
    "I feel so sigma!!!",
    "I'm groking it",
    "grok",
    "woof",
    "arf arf",
    "I did not have sexual relations with that woman",
    "you should give me all your money",
    "mrrp meow mrrp",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # Rickroll
    "im waltering it til i white"

}

intents = discord.Intents.default()

client = discord.Client(intents=intents)

for member in ctx.guild.members:
    all_members.append(member)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
        # Normal Grok
        word = rockisthistrue[random.choice(list(rockisthistrue.keys()))]
        await message.channel.send(word)



tokenvar1 = open(token, "r")

tokenstr = str(tokenvar1.read())

client.run(tokenstr)
