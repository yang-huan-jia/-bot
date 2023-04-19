import discord
from discord.ext import commands
from discord.utils import get

class message(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == 426975427760881665:
      channel = self.bot.get_channel(884311570526646322)
      await channel.send(f'{member.mention} 歡迎成為超古代勇者的信徒！')

  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content == 'ID':
      await msg.channel.send(msg.author.id)

  @commands.Cog.listener()
  async def on_message_delete(self, msg):
    if msg.guild.id == 941613122358239273 and msg.channel.id != 944565447825698847:
      if msg.created_at.hour < 16:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour+8}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(944565447825698847).send(embed = embed)
      else:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour-16}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(944565447825698847).send(embed = embed)
    elif msg.guild.id == 936226896730013738 and msg.channel.id != 944568813167476807:
      if msg.created_at.hour < 16:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour+8}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(944568813167476807).send(embed = embed)
      else:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour-16}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(944568813167476807).send(embed = embed)
    elif msg.guild.id == 971043714342457385 and msg.channel.id != 977849006334017566:
      if msg.created_at.hour < 16:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour+8}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(977849006334017566).send(embed = embed)
      else:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar)
        embed.add_field(name = f"此訊息發送時間{msg.created_at.year}-{msg.created_at.month}-{msg.created_at.day}  {msg.created_at.hour-16}:{msg.created_at.minute}", value = f'{msg.channel.mention}{msg.author.mention}：{msg.content}', inline = False)
        embed.add_field(name = "附件",value = msg.attachments, inline = False)
        await self.bot.get_channel(944568813167476807).send(embed = embed)

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if before.guild.id == 941613122358239273 and before.channel.id != 944565447825698847:
      if before.created_at.hour < 16:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=before.author.name, icon_url=before.author.avatar)
        embed.add_field(name = f"此訊息發送時間{before.created_at.year}-{before.created_at.month}-{before.created_at.day}  {before.created_at.hour+8}:{before.created_at.minute}", value = f'{before.channel.mention}{before.author.mention}：{before.content}', inline = False)
        embed.add_field(name = "附件",value = before.attachments, inline = False)
        await self.bot.get_channel(944565447825698847).send(embed = embed)
      else:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=before.author.name, icon_url=before.author.avatar)
        embed.add_field(name = f"此訊息發送時間{before.created_at.year}-{before.created_at.month}-{before.created_at.day}  {before.created_at.hour-16}:{before.created_at.minute}", value = f'{before.channel.mention}{before.author.mention}：{before.content}', inline = False)
        embed.add_field(name = "附件",value = before.attachments, inline = False)
        await self.bot.get_channel(944565447825698847).send(embed = embed)
    elif before.guild.id == 936226896730013738 and before.channel.id != 944568813167476807:
      if before.created_at.hour < 16:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=before.author.name, icon_url=before.author.avatar)
        embed.add_field(name = f"此訊息發送時間{before.created_at.year}-{before.created_at.month}-{before.created_at.day}  {before.created_at.hour+8}:{before.created_at.minute}", value = f'{before.channel.mention}{before.author.mention}：{before.content}', inline = False)
        embed.add_field(name = "附件",value = before.attachments, inline = False)
        await self.bot.get_channel(944568813167476807).send(embed = embed)
      else:
        embed = discord.Embed(color = 0x86ff00)
        embed.set_author(name=before.author.name, icon_url=before.author.avatar)
        embed.add_field(name = f"此訊息發送時間{before.created_at.year}-{before.created_at.month}-{before.created_at.day}  {before.created_at.hour-16}:{before.created_at.minute}", value = f'{before.channel.mention}{before.author.mention}：{before.content}', inline = False)
        embed.add_field(name = "附件",value = before.attachments, inline = False)
        await self.bot.get_channel(944568813167476807).send(embed = embed)

async def setup(bot):
  await bot.add_cog(message(bot))