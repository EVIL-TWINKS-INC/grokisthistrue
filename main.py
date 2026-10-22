import discord
import os
import random

BASE_DIR = r"/home/elly/leaked build of grok i stole from elons bootyhole"
IMAGES = os.path.join(BASE_DIR, "images")
token = os.path.join(BASE_DIR, "token.txt")

GOSSIP = [
    "gossip"
]

rockisthistrue = {
    # I don't know / maybe
    "idk",
    "Perhaps...",
    "Maybe.",
    "Maybe, I don't know. I kinda like to take things slow.",

    # Yes
    "Yes!",
    "I think so.",
    "Absolutely.",
    "Yes...?",
    "yuh uh",
    "Yeah but that's woke.",

    # No
    "No!",
    "Nein!",
    "Nope!",
    "No Way!",
    "Nah!",
    "nuh uh",
    "No, but I like your style!",

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

    # ADHD
    "Sometimes i think about a bunch of hot buff men dominating me.",
    "i am grok",
    "I feel so sigma!!!",
    "I'm groking it",
    "grok",
    "woof",
    "arf arf",
    "I did not have sexual relations with that woman",

}

gossips = {
    "gay",
    "trans",
    "woke",
    "conservative",
    "liberal",
    "texan",
    "cool",
    "a robot",
    "green",
    "evil",
}

intents = discord.Intents.default()

client = discord.Client(intents=intents)

for member in ctx.guild.members:
    all_members.append(member)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):

        # Random "[user] is [thing]" messages
        for word in GOSSIP:
            ping = random.choice(all_members)
            gossip = random.choice(gossips)
            if has_word(content, word):
                await message.channel.send(f"{ping.mention} is {gossip}")
                return


        # Normal Grok
        word = rockisthistrue[random.choice(list(rockisthistrue.keys()))]
        image = random.choice(os.listdir(IMAGES))
        image = os.path.join(IMAGES, image)
        if random.random() <= 0.2:
            await message.channel.send(
                word,
                file=discord.File(image)
            )
        else:
            await message.channel.send(word)



tokenvar1 = open(token, "r")

tokenstr = str(tokenvar1.read())

client.run(tokenstr)