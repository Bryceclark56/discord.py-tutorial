import random, os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class MyBot(commands.Bot):
    async def on_ready(self):
        print(f'Connected to Discord as {self.user}')


bot = MyBot(command_prefix='!')

@bot.command()
async def ping(ctx):
    """Check the bot's responsiveness"""

    await ctx.reply('Pong!')


compliments = [
    '{} has a great sense of humor!',
    '{} is awesome!',
    '{} is even more beautiful on the inside than on the outside.',
    '{} is an inspiration to us all.',
    '{} is like a ray of sunshine on a dreary day.',
    '{} is okay.'
]

@bot.command()
async def compliment(ctx, user: discord.Member):
    """Compliments the specified user :)"""

    compliment = random.choice(compliments).format(user.display_name)
    await ctx.send(compliment)

@compliment.error
async def compliment_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('You need to tell me who to compliment!')
    elif isinstance(error, commands.BadArgument):
        await ctx.reply('That\'s not a user in this server!')


@bot.command()
async def info(ctx, user: discord.Member):
    """Displays information about the specified user in an embed"""

    embed = discord.Embed(
        title=f'{user.name}#{user.discriminator}',
        description=f'''{f'**Nickname**: {user.nick}' if user.nick == None else ''}
        **ID**: {user.id}''',
        color=0x9800BE
    )

    embed.set_thumbnail(url=user.avatar_url)

    jt = user.joined_at
    embed.add_field(name='Joined:', value='{}\n{}'.format(jt.strftime('%m/%d/%Y'), jt.strftime('%H:%M:%S')))

    ct = discord.utils.snowflake_time(user.id)
    embed.add_field(name='Created:', value='{}\n{}'.format(jt.strftime('%m/%d/%Y'), ct.strftime('%H:%M:%S')))

    # Removes the first role in the list, which is @everyone, 
    #   and gets their mention strings.
    role_pings = [role.mention for role in user.roles[1:]]

    embed.add_field(name=f'Roles ({len(user.roles)}):', value=f'{" ".join(role_pings)}', inline=False)

    await ctx.send(embed=embed)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply('Invalid user provided.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('You must specify a user!')


bot.run(os.environ.get('DISCORD_BOT_TOKEN'))