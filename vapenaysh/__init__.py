from .vapenaysh import VapeNaysh
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(VapeNaysh(bot))
