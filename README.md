# Discord Bot Tutorial with Python

We assume that you are using Windows 10, and the example IDE/Editor will be [Visual Studio Code](https://code.visualstudio.com/).

## Git Setup

Create GitHub repo & clone locally.

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
    2. Open *PowerShell* in the current folder by pressing `Shift + Right Click` and selecting "Open command window here".
    3. In PowerShell, enter:

        ``` PowerShell
        git clone https://github.com/YourUsername/RepositoryName
        ```

        * Replace *YourUsername* and *RepositoryName* with the appropriate values

## Python setup


Install the latest python version (Python 3.9 at time of writing)

1. [Install Python](https://www.python.org/downloads/)

2. Create a virtual environment
    * Create in the git repo folder

3. Install required packages inside the virtual environment
    * Discord.<span></span>py

## IDE Setup


Experienced users may have a preferred environment, but this tutorial will be working under the assumption of you using Visual Studio Code on Windows 10.

(IMAGES OF WHERE TO INSTALL EXTENSIONS)

### Python Extension

### GitLens

### Opening the Project

1. Click on "Open Folder" in the *Welcome* tab of Visual Studio Code.
2. Navigate to where the cloned Git repository is located.
3. Click on the folder and hit okay.

### Virtual Environment

## Creating the Bot

**Please type the code examples, do not copy and paste them.**

In Visual Studio Code, create a new file and name it `bot.py`.
(INCLUDE IMAGE TO LOCATE NEW FILE BUTTON)

### Creating the Bot Class

1. Begin your bot by creating a class for it:

    ``` Python
    import discord

    class MyBot(discord.Client):
    ```

2. Add methods for *on_ready* and *on_message* after the class definition:

    ``` Python
    class MyBot(discord.Client):
        async def on_ready(self):
            print('Connected to Discord as {0}'.format(self.user))
        
        async def on_message(self, message):
            print('New message from {0.author}: {0.content}'.format(message))
    ```

### Connecting to Discord

1. Register your bot with Discord

    In-order to allow your bot to connect to Discord, you must create the bot user on the [Discord Developer Portal](https://discord.com/developers/)

    1. Create a new application
    2. Enable bot
    3. Copy token

## Adding Commands


### Ping

### Help

### User Input

------------------------------------

## Additional Resources


* [Python Documentation](https://www.python.org/doc/)
    * [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
* [Discord API Documentation](https://discord.com/developers/docs/intro)
