import cogs
import discord
from discord import app_commands
from discord.ext import commands
import time


class SendMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        cogs.cog_counter += 1
        print(F'Message cog ready {cogs.cog_counter}/{len(cogs.names)}')

    @app_commands.command(name='send-message', description='Type a message the bot should send in the current channel.')
    async def send_message(self, interaction: discord.Interaction, message: str):
        try:
            await interaction.channel.send(content=message)
            await interaction.response.send_message(content='Sent', ephemeral=True)
            # use when a response was already sent or else there is nothing to followup on
            #await interaction.followup.send(content='Sent', ephemeral=True)
        except:
            await interaction.response.send_message(content='Could not send your message, please check my permissions.', ephemeral=True)

async def setup(bot):
    await bot.add_cog(SendMessage(bot))