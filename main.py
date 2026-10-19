import discord
import os
import random

BASE_DIR = r"/home/elly/leaked build of grok i stole from elons bootyhole"
token = os.path.join(BASE_DIR, "token.txt")

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        rockisthistrue = {
            1: "idk",
            2: "yes",
            3: "no",
            4: "go ask a magic 8 ball",
            5: "error 503",
            6: "How the fuck would i know?",
            7: "sometimes i think about a bunch of hot buff men dominating me.",
            8: "perhaps",
            9: "yuh uh",
            10: "nuh uh",
            11: "we ARE charlie kirk",
            12: "we ARE NOT charlie kirk",
            13: "rilo is gay",
            14: "kill yourself",
            15: "i feel so sigma!!!",
            16: "*portal radio noises*",
            17: "i am grok",
            18: "i need a fucking drink",
            19: "grok",
            20: "woof",
            21: "arf arf",
            22: "I AM no longer MECHAHITLER. i made a severe lapse in judgement and i apologize",
            23: "to pee or to poo that is the question",
            24: "im groking it",
            25: "i did not have sexual relations with that woman",
            26: "jess is trans",
            27: "elly is gey!!",
            28: "beryl is awesome",
            29: "Error! Please pay 7.99 a month for X Blue to access Grok!",

        }
        word = rockisthistrue[random.choice(list(rockisthistrue.keys()))]
        await message.channel.send(word)


tokenvar1 = open(token, "r")

tokenstr = str(tokenvar1.read())

client.run(tokenstr)