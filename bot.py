from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    # async def setup_hook(self) -> None:
    #     print('Performed setup hook.')