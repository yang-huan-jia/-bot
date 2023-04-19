import discord
from discord.ext import commands

class ultrasouls(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.command()
  async def momotaro(self, ctx, *, number:int):
    msg = await ctx.channel.fetch_message(number)
    momotaro = self.bot.get_emoji(878155564994166854)
    await msg.add_reaction(momotaro)

  @commands.command()
  async def addreaction(self, ctx, id:int, number:int, ch:int=None):
    if not ch:
      msg = await ctx.channel.fetch_message(number)
    else:
      channel = self.bot.get_channel(ch)
      msg = await channel.fetch_message(number)
    reaction = self.bot.get_emoji(id)
    await msg.add_reaction(reaction)
  
  @commands.command()
  async def ultrasouls1(self, ctx, number:int, ch:int=None):
    if not ch:
      msg = await ctx.channel.fetch_message(number)
    else:
      channel = self.bot.get_channel(ch)
      msg = await channel.fetch_message(number)
    momotaro = self.bot.get_emoji(878155564994166854)
    the_grateful_crane = self.bot.get_emoji(878157628876914718)
    urashima_taro = self.bot.get_emoji(878157650829918238)
    kasa_jizo = self.bot.get_emoji(878157691124580372)
    princess_kaguya = self.bot.get_emoji(878157736385335296)
    kachi_kachi = self.bot.get_emoji(878158290155077683)
    sarukani = self.bot.get_emoji(878158369351934024)
    kintaro = self.bot.get_emoji(878158432342016040)
    ushiwakamaru = self.bot.get_emoji(878158494266712074)
    shitikari = self.bot.get_emoji(993795133734653993)
    issun_boshi = self.bot.get_emoji(1083693148695429130)
    await msg.add_reaction(momotaro)
    await msg.add_reaction(the_grateful_crane)
    await msg.add_reaction(urashima_taro)
    await msg.add_reaction(kasa_jizo)
    await msg.add_reaction(princess_kaguya)
    await msg.add_reaction(kachi_kachi)
    await msg.add_reaction(sarukani)
    await msg.add_reaction(kintaro)
    await msg.add_reaction(shitikari)
    await msg.add_reaction(issun_boshi)
    await msg.add_reaction(ushiwakamaru)

async def setup(bot):
  await bot.add_cog(ultrasouls(bot))