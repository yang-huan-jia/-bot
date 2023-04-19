import discord
from discord.ext import commands
import asyncio

class ordinary(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def ping(self,ctx):#延遲指令
    await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')
  
  @commands.command()
  async def avatar(self,ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar
    await ctx.send(userAvatar)

  @commands.command()
  async def clean (self,ctx, num:int):
    if ctx.author.id == 426974412428804097:
      await ctx.channel.purge(limit=num)
  
  @commands.command()
  async def kick (self,ctx, member:discord.Member, *, reason=None):
    if ctx.author.id == 426974412428804097:
      await member.kick(reason=reason)
      await self.bot.get_channel(884312764200411157).send(f'{member.mention}已被踢出')
  
  @commands.command()
  async def ban (self,ctx, member:discord.Member, *, reason=None):
    if ctx.author.id == 426974412428804097:
      await member.ban(reason=reason)
      await self.bot.get_channel(884312764200411157).send(f'{member.mention}已被停權，並且不得再次加入此伺服器')

  @commands.command()
  async def timer(self,ctx, time:int, *, msg):
    while True:
      await asyncio.sleep(time)
      await ctx.send(f'{msg}, {ctx.author.mention}')
      break

async def setup(bot):
  await bot.add_cog(ordinary(bot))