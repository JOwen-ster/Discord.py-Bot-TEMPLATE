# Discord.py-Bot-TEMPLATE
A repo containing a standard file structure template for a Discord bot!
- Written using [**__Discord.py__**](https://github.com/Rapptz/discord.py)
  - Read the docs [**__here__**](https://discordpy.readthedocs.io/en/stable/)

# Content
- [X] Cogs Directory
- [X] Utils Directory
- [X] Custom Bot Class
- [X] Main File
```
Template/
├─── cogs/
│    ├─── __init__.py
│    ├─── cog1.py
│    ├─── cog2.py
│    ├─── cog3.py
│    ├─── ...
├─── utils/
│    ├─── __init__.py
│    ├─── util1.py
│    ├─── util2.py
│    ├─── util3.py
│    ├─── ...
├─── __init__.py
├─── .env
├─── bot.py
├─── __main__.py
```
> [!NOTE]
> Cogs are used to organize a collection of commands, listeners, and some state into one class. [Cogs Documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

> [!NOTE]
> Utils are helpers or reusable assets.

> [!NOTE]
> Bot file is used to create a custom Discord Bot Client. This lets you import your bot into different files and make calls when your Client is created.
