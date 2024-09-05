import cogs
import discord
from discord import app_commands
from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        cogs.cog_counter += 1
        print(F'Purge cog ready {cogs.cog_counter}/{len(cogs.names)}')

    @app_commands.command(name='send-message', description='Purge messages.')
    async def send_message(self, interaction:discord.Interaction, message:str):
        try:
            await interaction.channel.send(content=message)
            await interaction.followup.send(content='Sent', ephemeral=True)
        except:
            await interaction.followup.send(content='Could not send your message, please check my permissions.', ephemeral=True)

async def setup(bot):
    await bot.add_cog(Purge(bot))