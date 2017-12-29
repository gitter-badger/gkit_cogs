from .flavorsavor import FlavorSavor
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(FlavorSavor(bot))
