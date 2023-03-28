from discord.ext import commands

from cfg import TOKEN
from events import Events
from commands import Commands


bot = commands.Bot()
bot.add_cog(Commands(bot))
bot.add_cog(Events(bot))
bot.run(TOKEN)
