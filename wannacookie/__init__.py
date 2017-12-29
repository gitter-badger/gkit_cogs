from .wannacookie import WannaCookie
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(WannaCookie(bot))
