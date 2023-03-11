from discord.ext import commands
from discord import Activity, ActivityType


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {}!'.format(self.bot.user))
        await self.bot.change_presence(
            activity=Activity(type=ActivityType.playing, name="ip: dreammc.su"))
