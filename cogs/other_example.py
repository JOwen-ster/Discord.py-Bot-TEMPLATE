from cogs import names
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from utils.infoformmodal import InfoModal
from utils.embeds import BotConfirmationEmbed
from utils.embeds import reminderEmbed
from utils.loggingsetup import getlog

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='remindme', description='Reminds at a specific time once')
    @app_commands.describe(title='Title of the reminder',
                        date='Insert date as MM/DD/YY',
                        time='Insert time as XX:XX using a 12-hour clock',
                        details='Description of reminder',
                        reminder='Insert time as XX:XX of when to be reminded',
                        location='Location of reminder (optional)')
    async def createReminder(self, interaction: discord.Interaction,
                        title: str, 
                        date: str, 
                        time: str,
                        details: str,
                        reminder: str,
                        location: str = "N/A"):

        embed = reminderEmbed(embed_title=title,
                            date=date,
                            time=time,
                            details=details,
                            reminder=reminder,
                            location=location
        )
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(
            embed=BotConfirmationEmbed(description='Sent'),
            ephemeral=True
        )

# Add the cog to your discord bot.
async def setup(bot):
    await bot.add_cog(Reminders(bot))