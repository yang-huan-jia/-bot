import discord
from discord.ext import commands
import json
import random
import nacl

class role(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  async def addrole(self, ctx, role: discord.Role):
    if role.id == 859634262068035595 or role.id ==907146631407869992:
      await ctx.author.add_roles(role)
      await ctx.send(f" {ctx.author.mention} 已獲得  {role.mention} 身份組")

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.member.bot:
      pass
    else:
      with open('reactrole.json', 'r', encoding = 'utf8')as f:
        reactrole = json.load(f)
        for x in reactrole:
          if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
            role = discord.utils.get(self.bot.get_guild(payload.guild_id).roles, id = x['role_id'])
            await payload.member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
      with open('reactrole.json', 'r', encoding = 'utf8')as f:
        reactrole = json.load(f)
        for x in reactrole:
          if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
            role = discord.utils.get(self.bot.get_guild(payload.guild_id).roles, id = x['role_id'])
            await self.bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

  @commands.command()
  async def reactrole(self, ctx, emoji, role: discord.Role, *, message):
    embed = discord.Embed(description = message,color = 0x86ff00)
    msg = await ctx.channel.send(embed = embed)
    await msg.add_reaction(emoji)
    
    with open('reactrole.json', 'r', encoding = 'utf8')as f:
      reactrole = json.load(f)

      new_react_role ={    
        "role_name": role.name,
        "role_id": role.id,
        "emoji": emoji,
        "message_id": msg.id
      }

      reactrole.append(new_react_role)

    with open('reactrole.json', 'w', encoding = 'utf8')as f:
      json.dump(reactrole, f,indent = 4)

  @commands.command()
  async def addreactrole(self, ctx, emoji, role: discord.Role, *, number:int):
    msg = await ctx.channel.fetch_message(number)
    await msg.add_reaction(emoji)
    
    with open('reactrole.json', 'r', encoding = 'utf8')as f:
      reactrole = json.load(f)

      new_react_role ={    
        "role_name": role.name,
        "role_id": role.id,
        "emoji": emoji,
        "message_id": number
      }

      reactrole.append(new_react_role)

    with open('reactrole.json', 'w', encoding = 'utf8')as f:
      json.dump(reactrole, f,indent = 4)
  
  @commands.command()
  async def addmomotaro(self, ctx, *, number:int):
    msg = await ctx.channel.fetch_message(number)
    momotaro = self.bot.get_emoji(878155564994166854)
    await msg.add_reaction(momotaro)
    


async def setup(bot):
  await bot.add_cog(role(bot))