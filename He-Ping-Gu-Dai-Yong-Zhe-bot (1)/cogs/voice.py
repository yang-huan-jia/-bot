import discord
from discord.ext import commands
import asyncio
import os
import nacl
import DiscordUtils

class voice(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def join(self,ctx):
    await ctx.author.voice.channel.connect()

  @commands.command()
  async def leave(self,ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self,ctx, *, url):
    music = DiscordUtils.Music()
    player = music.get_player
    await ctx.voice_client.disconnect(guild_id = ctx.guild.id)
    if not player:
      player = music.create_player(ctx, ffmpeg_error_betterfix = True)
    if not ctx.voice_client.is_playing():
      await player.queue(url, search = True)
      song =  await player.play()
      await ctx.send(f'已開始播放 {song.name} ')
    else:
      song = await player.queue(url, search  = True)
      await ctx.send(f'已將 {song.name} 加入播放列表')

    
async def setup(bot):
  await bot.add_cog(voice(bot))