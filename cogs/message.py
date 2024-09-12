import cogs
import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import BotEmbedMessage
from utils.embeds import BotEmbedConfirmation
from utils.embeds import BotEmbedError


class SendMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        cogs.cog_counter += 1
        print(F'Message cog ready {cogs.cog_counter}/{len(cogs.names)}')
        
    # slash command example
    @app_commands.command(name='send-message', description='Type a message the bot should send in the current channel.')
    async def send_message(self, interaction: discord.Interaction, message: str):
        try:
            emb_message = BotEmbedMessage(description=message)
            emb_confirm = BotEmbedConfirmation(description='Message sent!')
            await interaction.channel.send(embed=emb_message)
            await interaction.response.send_message(embed=emb_confirm, ephemeral=True)
            # use when a response was already sent or else there is nothing to followup on
            #await interaction.followup.send(content='Sent', ephemeral=True)
        except:
            emb_error = BotEmbedError(description='Could not send your message, please check my permissions.')
            await interaction.response.send_message(embed=emb_error, ephemeral=True)

async def setup(bot):
    await bot.add_cog(SendMessage(bot))