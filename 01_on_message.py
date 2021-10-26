import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    await message.channel.send('yo')


client.run('ODM0MTg5NjQ2NTQyOTI5OTcx.YH9Rpg.fvVzDQ9HnXlcBtuOpwY1a8dcVzg')