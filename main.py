import discord
import os
BASE_DIR = r"C:\Users\Admin\PycharmProjects\grokisthistrue"
token = os.path.join(BASE_DIR, "token.txt")


intents = discord.Intents.default()


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Source - https://stackoverflow.com/a/66719286
# Posted by Andhavarapu Balu, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-16, License - CC BY-SA 4.0

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send('You mentioned me!')


tokenvar1 = open(token, "r")

tokenstr = str(tokenvar1.read())

client.run(tokenstr)