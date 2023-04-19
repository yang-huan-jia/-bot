import discord
from discord.ext import commands
from discord.utils import get
import json
import aiosqlite
import random

class level2(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def level(self, ctx, member: discord.Member = None):
    if member is None:
      member = ctx.author
    async with self.bot.db.cursor() as cursor:
      await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id,))
      xp = await cursor.fetchone()
      await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id,))
      level = await cursor.fetchone()
      try:
        xp=xp[0]
        level=level[0]
      except TypeError:
        xp = 0
        level = 0
      embed = discord.Embed(title = f"{member.display_name}的等級", description = f"等級：{level}\n 經驗值：{xp}/{round((10*(level+1) ** (0.06*level))+ level*47)}")
      await ctx.send(embed=embed)
    

async def setup(bot):
  await bot.add_cog(level2(bot))