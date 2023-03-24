from discord.ext import commands

from cfg import TOKEN, PREFIX
from events import Events
from commands import Commands


bot = commands.Bot(command_prefix=PREFIX)
bot.add_cog(Commands(bot))
bot.add_cog(Events(bot))
bot.run(TOKEN)
