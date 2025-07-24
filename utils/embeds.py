from discord import Embed, Color


class BotExampleEmbed(Embed):
    def __init__(self, *args, **kwargs):
        # Use default arguments for the inherited embed class
        # Overload color to always be black ( rgb(0,0,0) ) unless changed after object declaration
        super().__init__(color=Color.default(), *args, **kwargs)


class BotMessageEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.from_rgb(0,0,0), *args, **kwargs)


class BotConfirmationEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.green(), *args, **kwargs)


class BotErrorEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=Color.red(), *args, **kwargs)


def reminderEmbed(embed_title: str, **fields):
    embed = Embed(
        title=embed_title,
        color=Color.red(),
    )
    for key, value in fields.items():
        embed.add_field(name=f'{key}', value=f'{value}', inline=False)
    return embed