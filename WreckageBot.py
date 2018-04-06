# https://github.com/alwaysafk/WreckageBot.git
import discord

TOKEN = 'NDMxODEzMjQzNDQ3NTQxNzYx.DakM-Q.MUC_R3YLzUzyb5ynRXH-S8WZAEQ'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif 'good bot' in message.content.lower():
        msg = 'I\'ll suck yo dick'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!'):
        msg = 'WHAT I DON\'T UNDERSTAND'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)