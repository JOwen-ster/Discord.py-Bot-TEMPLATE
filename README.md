# Discord.py-Bot-TEMPLATE
A repo containing a standard file structure template for a Discord bot!
- Written using [**__Discord.py__**](https://github.com/Rapptz/discord.py)
  - Read the docs [**__here__**](https://discordpy.readthedocs.io/en/stable/)

[**TODO LIST**📋](/TODO.md)

# Content
- [X] Cogs Directory
- [X] Database Directory
- [X] Utils Directory
- [X] Custom Bot Class
- [X] Runner File
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
├─── .env
├─── botclient.py
├─── run_bot.py
```
> [!NOTE]
> Cogs are used to organize a collection of commands, listeners, and some state into one class. [Cogs Documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

> [!NOTE]
> Utils are helper methods or reusable assets.

> [!NOTE]
> Bot file is used to create a custom Discord Bot Client. This lets you import your bot into different files and make calls when your Client is created.

# **You will need...**
- A [Discord](https://discord.com/) account
- [Python](https://www.python.org/) installed
  - If you want to use JavaScript to make a Discord bot, I recommend using this [template](https://github.com/PillowGit/base-discord-js-bot) made by [@PillowGit](https://github.com/PillowGit) for the coding portion
- Internet access
- A IDE to edit and run code (Like Visual Studio Code)


***CLONE THIS REPOSITORY***
- [x] HTTPS
```
git clone https://github.com/JOwen-ster/Discord.py-Bot-TEMPLATE.git
```

- [X] SSH
```
git clone git@github.com:JOwen-ster/Discord.py-Bot-TEMPLATE.git
```

- [X] GitHub CLI
```
gh repo clone JOwen-ster/Discord.py-Bot-TEMPLATE
```

![Discord_Python_Logo](https://images.opencollective.com/discordpy/25fb26d/logo/256.png)

## Creating Your Application
Head over to the [discord developer page](https://discord.com/developers/applications), log in, and at the top right of your screen click `New Application`, type the name of your Discord bot, and then click `create`

> [!NOTE]
> For simplicity we will not select a team, but you can create a team in the 'Teams' tab and add people that will be associated with the development of the bot!

On the side, click on the `Bot` tab and then scroll down to `Privileged Gateway Intents` on that page. These are the different types of data that your bot will have access to when in a server. You can read about them on [developer gateway intents page](https://discord.com/developers/docs/topics/gateway#gateway-intents) to see what each intent covers and if you may need a single or multiple when you make your own bot!

> [!NOTE]
> For simplicity, we will toggle on all gateway intents in case you want to add more to your first bot. In real practice, you want to read up on these intents and see which your bot would need since when you apply to get your bot verified at 75 servers, Discord will ask you why you are using them! You will need to apply for gateway intents separately with the verification process. If you have any questions about verifying a discord bot, ask me on Discord (`typos.`) since I have a bot that is in 300+ servers and is verified!

Next, on the side of your screen click on the `Installation` tab.

* Scroll down to the `Install Link` dropdown menu, make sure `Discord Provided Link` is selected.

Now, scroll down to `Default Install Settings` and click on the `SCOPES` dropdown menu under `Guild Install`.
* Under the `SCOPES` -> select `bot`.
* Under `PERMISSIONS` -> select any server permissions that your bot will need to fully function.

> [!NOTE]
> For this workshop we will use the `Administrator` permission for ease. Giving a user or bot `Administrator` will give access to all channels with all permissions regardless of how they are setup in your server.
> Bots are treated like regular members in a server with their access to channels and ways they interact with the server. For example able to `manage member` is not a usual default permission for most servers, it will not be for a bot unless you give it that permission.

> [!WARNING]
> Unless your Discord bot's function is for server management such as raid protection, server setup, moderation, or various non member interactive things, I would **NOT** set your permission to `Administrator` just because it is "easy". From my bot developing experience, when getting bots into bigger servers, some owners really wanna limit what it can do for security purposes. As an example, if your token gets exposed, someone logs into your bot and with a total of 20 lines of code (not joking) every server that bot is in, it will nuke, mass ping, and ban every member.

Under `Install Link`, there is a link you send to others. When clicked, that user can add your bot with all the permissions you selected to any server they have the `Manage Server` permission in (or it will not appear under the list of servers when adding).


### Before we get coding...
> [!IMPORTANT]
> Go to the `Bot` tab.
> Click `Reset Token` near the top of the page

# ***__COPY AND SAVE THIS TOKEN SOMEWHERE SECURE AND SOMEWHERE YOU CAN ACCESS IT__***

> [!CAUTION]
> # **THIS TOKEN IS HOW TO CONNECT TO YOUR APPLICATION WITH CODE, NO ONE NEEDS ANYTHING ELSE TO CONNECT/LOG INTO YOUR BOT EXCEPT THE MOST RECENT TOKEN. NEVER POST IT OR YOU RISK YOUR BOT GETTING HIJACKED**

> [!CAUTION]
> If you do not type `.env` in your `.gitignore` file, (the `.env` file is where you should put your token) , then GitHub bots **will** scrape your token (it has happened to me) and may use it. Discord will hopefully send you a message very fast saying they caught it and reset it since they are also scraping for Discord Bot Tokens to watch out for you and keeping your bots secure :)

![image](https://github.com/JOwen-ster/Discord_Bot_Workshop_2024/assets/111905194/79737d0c-b11f-4ee2-a0e2-f23a2d7f92f7)

## Coding the Actual Discord Bot
By the end, you will have a bot that has a simple slash command that sends messages in an embed, a simple slash command that uses a modal/form, a simple slash command that has buttons and a dropdown menu, a background task that will always be updating the bots Discord status to display how many servers it is in, and a logging setup for all actions the bot does.
We will be using the [discord.py](https://discordpy.readthedocs.io/en/stable/) API wrapper in this workshop.

[Read the docs (How to do Commands)](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)

[Read the docs (How to do Events/Listeners)](https://discordpy.readthedocs.io/en/stable/api.html?highlight=event#discord-api-events)

First, activate a virtual ENV by running this command once you have changed directory to this repository.
```
python -m venv botenv
```

Then (only for Windows Powershell Users)
```
Set-ExecutionPolicy RemoteSigned
```

```
.\botenv\Scripts\Activate.ps1
```

For Linux users
```
source botenv/bin/activate
```

Then, install all requirements and dependancies from the requirements.txt in this repo...
```
pip install -r requirements.txt
```

After you have successfully installed the libraries...

## **Open your favorite code IDE!**

Create a new file named `.env` (no name before the dot) and put the following in it.

```
DISCORD_BOT_TOKEN = 'YOUR_BOT_TOKEN_GOES_HERE'
```

Normally you would create a new file named `.gitignore` and put the following inside it.
```
.env
```

I have already done this for you so all you need to do is add more cogs/functionality and then run [run_bot.py](/run_bot.py)!
