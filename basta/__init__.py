from .basta import BASTA
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(BASTA(bot))
