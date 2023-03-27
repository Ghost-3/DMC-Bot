from discord.ext import commands
from discord import Activity, ActivityType
from asyncio import sleep

from utils.server_status import ServerStatus


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.server_status: ServerStatus = ServerStatus()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {}!'.format(self.bot.user))
        while True:
            status = self.server_status.get_status()
            online = status.players.online if status else 0
            await self.bot.change_presence(
                activity=Activity(type=ActivityType.watching, name="Онлайн {}".format(online)))
            await sleep(60)
