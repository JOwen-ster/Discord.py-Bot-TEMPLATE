import discord
from discord import app_commands
from discord.ext import commands
from cogs import extensions
from utils.embeds import BotConfirmationEmbed
from utils.embeds import createEmbedFields
from utils.loggingsetup import getlog


class EmbedMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.cog_counter += 1
        getlog().info(F'{__name__} ready ({self.bot.cog_counter}/{len(extensions)})')

    @app_commands.command(name='post', description='Create a embed with your own fields')
    @app_commands.describe(title='Title',
                        date='Insert a date as MM/DD/YY',
                        time='Insert a time as XX:XXam/pm using a 12-hour clock',
                        details='Insert a description',
                        location='Location of reminder (optional)')
    async def createPost(self, interaction: discord.Interaction,
                        title: str, 
                        date: str, 
                        time: str,
                        details: str,
                        location: str = "N/A"):

        embed = createEmbedFields(embed_title=title,
                            date=date,
                            time=time,
                            details=details,
                            location=location
        )
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(
            embed=BotConfirmationEmbed(description='Sent'),
            ephemeral=True
        )

# Add the cog to your discord bot.
async def setup(bot):
    await bot.add_cog(EmbedMessage(bot))
