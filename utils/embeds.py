from discord import Embed, Color


class BotMessageEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.from_rgb(255,255,255), *args, **kwargs)


class BotConfirmationEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.green(), *args, **kwargs)


class BotErrorEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.red(), *args, **kwargs)


def createEmbedFields(embed_title: str, **fields):
    embed = Embed(
        title=embed_title,
        color=Color.red(),
    )
    for key, value in fields.items():
        embed.add_field(name=f'{key}', value=f'{value}', inline=False)
    return embed