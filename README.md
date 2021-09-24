# Discord Bot Tutorial with Python

We assume that you are using Windows 10, and the example IDE/Editor will be [Visual Studio Code](https://code.visualstudio.com/).

The following programs are required for this tutorial:

Program | Download Page
--------|--------------
Python 3.9 | <https://www.python.org/downloads/>
Git | <https://git-scm.com/downloads>
Visual Studio Code | <https://code.visualstudio.com/download>

## Python setup

Install the latest python version (Python 3.9 at time of writing).

1. [Install Python](https://www.python.org/downloads/)
    * When you see the option during installation, click the `Add to PATH` checkbox!

2. Restart your computer for some changes to take effect.

## Git Setup

Create a GitHub repo & clone locally.

1. If not already done, create a [GitHub](https://github.com/) account.

2. [Create a new repository](https://github.com/new) on GitHub and fill out the required fields.

    Dropdown located in the top-right of the GitHub website

    ![Click to create new repository](img/github_new_repo.png)

    ![Name your repository](img/github_repo_name.png)

    Click this button after naming your repository:

    ![Click this button last](img/github_repo_create.png)

    **Important**: You will be brought to a new page.
    Copy the URL in the box and save it somewhere for later.

    ![Copy and save this URL](img/github_repo_url.png)

3. [Install Git](https://git-scm.com/downloads) on your computer.

4. Clone the git repository to your computer

    1. In *File Explorer*, navigate to where you want to store your code. (Desktop, My Documents, etc.)

    2. Open *Command Prompt* in the current folder by pressing `Shift + Right Click` and selecting "Open command window here".

    3. In Command Prompt, enter:

        ``` CMD
        git clone https://github.com/YourGitHubUsername/RepositoryName
        ```

        * Replace *YourUsername* and *RepositoryName* with the appropriate values.

## IDE Setup

You can access the extensions section from the button on the left side of Visual Studio Code.

![Open the extensions tab](img/vscode_extensions_tab.png)

### Python Extension

1. Type `python` into the search bar.

    ![Search for python](img/vscode_extension_search_python.png)

2. Click the extension published by *Microsoft*. It should be the first in the list of results.

3. Click the blue install button.

### GitLens

1. Type `gitlens` into the search bar.

    ![Search for gitlens](img/vscode_extension_search_gitlens.png)

2. Click the extension `GitLens -- Git supercharged` by Eric Amodio. It should be the first in the list of results.

3. Click the blue install button.

### Opening the Project

1. Click on "Open Folder" in the *Welcome* tab of Visual Studio Code. (The tabs are located at the top of the window)

    * If you lost this tab, you can also use the *File* context menu in the top-left to perform this action.

2. Navigate to where the cloned Git repository is located.

3. Click on the folder and hit okay.

### Virtual Environment

1. Open a terminal in Visual Studio Code

2. Create the virtual environment

3. Install the required libraries

## Creating the Bot

**Please type the code examples, do not copy and paste them.**

**Indentation in the code is important!**

In Visual Studio Code, create a new file and name it `bot.py`.

![Click here to create a new file](img/vscode_new_file_button.png)

### Creating the Bot Class

1. Import the `discord.py` library:

    ``` Python
    import discord # Import discord.py
    ```

2. Create the class for your bot and an *on_ready* method:

    ``` Python
    class MyBot(discord.Client):
        async def on_ready(self): # on_ready method signature
            print(f'Connected to Discord as {self.user}') # on_ready method body
    ```

3. Instantiate the bot

    1. Import the `OS` module, allowing you to get environment variables.

        ``` Python
        import os # This should be at the top of the file, above or below the other import
        ```

    2. Create the bot variable, and pass in your *discord bot token* via an environment variable.

        ``` Python
        # This should be below everything else in the file
        bot = MyBot(command_prefix='!')
        bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
        ```

Your current `bot.py` file should look like:

``` Python
import discord
import os

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Connected to Discord as {self.user}')


bot = MyBot(command_prefix='!')
bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
```

### Connecting to Discord

1. Register your bot with Discord

    In-order to allow your bot to connect to Discord, you must create the bot user on the [Discord Developer Portal](https://discord.com/developers/).

    1. Create a new application

    2. Enable the bot user

    3. Copy the token

2. Invite the bot to your server

    1. Configure permissions

    2. Copy the invite link

    3. Paste in browser

    4. Allow the bot to join

3. Start the bot

    Now run the python program, allowing the bot to connect to Discord.

    * Don't forget to paste your bot token on the first line (where it says *YOUR_TOKEN*)

    ``` CMD
    set DISCORD_BOT_TOKEN=YOUR_TOKEN
    python bot.py
    ```

    You should see it say something similar to `Connected to Discord as BotName#0123` in your terminal. It may take a moment to appear.

    This means your bot has successfully connected to Discord and can interact with your server and its users!

## Adding Commands

Commands are the most basic way for users in your server to interact with your bot.

As you add each command, re-start your bot and test it out!

**Important**: Ensure that the code is typed before `bot.run()` and *after* `bot = MyBot()`

### Ping

A ping command is an easy way for users and yourself to ensure that your bot can read and reply to users' messages.

``` Python
@bot.command() # Links the function to your bot as the logic for the command
async def ping(ctx): # The command name is defined by the function name
    """Check the bot's responsiveness""" # Describes what the command

    await ctx.reply('Pong!') # Send's the message as a reply (notifies them) to the user
```

You can test the command by sending `!ping` into any channel in the Discord server with your bot.

And, __if you feel lost__, here is what you should have so far:

``` Python
import discord
import os

class MyBot(discord.Client):
    async def on_ready(self):
        print('Connected to Discord as {0}'.format(self.user))


bot = MyBot(command_prefix='!')

@bot.command()
async def ping(ctx):
    """Check the bot's responsiveness"""

    await ctx.reply('Pong!')


bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
```

### Compliment

We're going to introduce user input into your bot's commands.

This command will take in a user in your server and respond with a random compliment from a list.

### User Info

Now you're going to use an embed in your response!

These allow a more advanced formatting for your messages than a normal string provides.

------------------------------------

## Additional Resources

Feel free to browse these resources to learn more on the topics presented in this tutorial!

* [Python Documentation](https://www.python.org/doc/)
  * [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
* [Discord API Documentation](https://discord.com/developers/docs/intro)
