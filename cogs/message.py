import cogs
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from utils.embeds import BotMessageEmbed
from utils.embeds import BotConfirmationEmbed
from utils.embeds import BotErrorEmbed
from utils.loggingsetup import getlog


class SendMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Start Tasks
        self.updatestatus.start()

    @commands.Cog.listener()
    async def on_ready(self):
        cogs.cog_counter += 1
        getlog().info(F'Message cog ready ({cogs.cog_counter}/{len(cogs.names)})')

    # Slash command (application command) (tree command) example
    # IMPORTANT
    # USE TYPE HINTS FOR ALL PARAMETERS WITH COG SLASH COMMANDS (application commands)
    # OR ELSE SELF@class WILL BE PASSED AS THE INTERACTION
    # https://github.com/Rapptz/discord.py/discussions/8372

    @app_commands.command(name='send-message', description='Type a message the bot should send in the current channel.')
    async def send_message(self, interaction: discord.Interaction, message: str):
        try:
            emb_message = BotMessageEmbed(description=message)
            emb_confirm = BotConfirmationEmbed(description='Message sent!')
            await interaction.channel.send(embed=emb_message)
            await interaction.response.send_message(embed=emb_confirm, ephemeral=True)
            getlog().info(f'USED COG: {self.__cog_name__}')

            # use followup when a response was already sent or else there is nothing to followup on
            # await interaction.followup.send(content='Sent', ephemeral=True)
        except:
            emb_error = BotErrorEmbed(description='Could not send your message, please check my permissions.')
            try:
                await interaction.response.send_message(embed=emb_error, ephemeral=True)
            except discord.InteractionResponded:
                await interaction.followup.send(content='Sent', ephemeral=True)
            except:
                getlog().error('ERROR: failed to response to send-message interaction')
            finally:
                getlog().error('ERROR: Could not terminate send-message successfully')

    # Background task using the asyncio discord.ext tasks decorator
    @tasks.loop(minutes=1.0)
    async def updatestatus(self):
        await self.bot.change_presence(activity=discord.Game(name=F'in {len(self.bot.guilds)} servers'))
        getlog().info(F'RAN TASK: Update Status')

    @updatestatus.before_loop
    async def before_printer(self):
        getlog().info('TASK WAITING UNTIL READY: Update Status')
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(SendMessage(bot))