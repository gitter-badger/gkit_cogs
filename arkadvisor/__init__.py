from .arkadvisor import ArkAdvisor
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(ArkAdvisor(bot))
