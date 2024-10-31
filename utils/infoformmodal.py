import discord
from utils.loggingsetup import getlog


class InfoModal(discord.ui.Modal, title='InfoModal'):
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your name here...',
        required=True,
    )

    about = discord.ui.TextInput(
        label='About',
        style=discord.TextStyle.long,
        placeholder='Tell us about yourself...',
        required=True,
        max_length=200,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thank you for responding, {self.name.value}!', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('And error occured while submitting.', ephemeral=True)
        getlog.error(repr(error))