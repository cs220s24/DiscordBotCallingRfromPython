# bot.py
import os
import subprocess

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.messages = True  # Enables receiving messages
intents.guilds = True  # Enables guild-related events
intents.message_content = True

# Create a subclass of Client to handle events
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        guild = discord.utils.get(client.guilds, name=GUILD)
        channel = self.get_channel(1232853994175729737)  
        await channel.send("Hello I am the Chickwts plot bot!\nThese commands provide further info:\n- !options: Displays the plot commands I can run\n- !info: Provides informations about the dataset Chickwts")
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'Logged in as {self.user} (ID: {self.user.id})'

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Check for user message and displays appropriate response
        if message.content.startswith('!options'):
            await message.channel.send('These are the commands I can run:\n- !plot boxplot\n- !plot histogram\n- !plot barplot')
        elif message.content.startswith('!info'):
            await message.channel.send('The Chickwts dataset contains 71 observations on the following 2 variables:\n- weight: a numeric vector giving the body weight of the chicks\n- feed: a factor giving the feed type\nThe dataset is used in the examples of the book "Statistical Models in S" by Chambers and Hastie.')

        # Command to generate boxplot using R script
        elif message.content.startswith('!plot boxplot'):
            # Call the R script to generate the plot
            subprocess.run(['Rscript', 'generateBoxplot.R'], check=True)
            # Send the generated image to the channel
            with open('boxplot_chickwts.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send('Boxplot for the chickwts dataset:', file=picture)
            # Remove the PNG file after sending it
            os.remove('boxplot_chickwts.png')

	# Command to generate histogram using R Script
        elif message.content.startswith('!plot histogram'):
            subprocess.run(['Rscript', 'generateHistogram.R'], check=True)
            with open('histogram_chickwts.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send('Histogram for the chickwts dataset:', file=picture)
            # Remove PNG file after sending it
            os.remove('histogram_chickwts.png')
        
        # Command to generate barplot using R script
        elif message.content.startswith('!plot barplot'):
            # Call the R script to generate the plot
            subprocess.run(['Rscript', 'generateBarplot.R'], check=True)
            # Send the generated image to the channel
            with open('barplot_chickwts.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send('Barplot for the chickwts dataset:', file=picture)
            # Remove the PNG file after sending it
            os.remove('barplot_chickwts.png')
	
# Create an instance of the client and run it
client = MyClient(intents=intents)
client.run(TOKEN)

