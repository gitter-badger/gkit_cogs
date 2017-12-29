from .pep20 import BDFL
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(BDFL(bot))
