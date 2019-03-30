
import discord, config

discord_token = config.discord_token
discord_client_id = config.discord_client_id
discord_client_secret = config.discord_client_secret

client = discord.Client()

@client.event
async def on_message(message):
	if message.content.find('!hello') != -1:
		await message.channel.send("hi")

client.run(discord_token)