import discord


class BotEmbedExample(discord.Embed):
    def __init__(self, *args, **kwargs):
        # Use default arguments for the inherited embed class
        # Overload color to always be black ( rgb(0,0,0) ) unless changed after object declaration
        super().__init__(color=discord.Color.default(), *args, **kwargs)

class BotEmbedMessage(discord.Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=discord.Color.from_rgb(0,0,0), *args, **kwargs)

class BotEmbedConfirmation(discord.Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=discord.Color.green(), *args, **kwargs)


class BotEmbedError(discord.Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(color=discord.Color.red(), *args, **kwargs)