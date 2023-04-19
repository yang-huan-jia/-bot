import discord
from discord.ext import commands
from discord.utils import get
import json
import random

class level(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    async def update_data(users, user):
      if not f'{user.guild.id}' in users:
        users[f'{user.guild.id}'] = {}
      if not f'{user.id}' in users[f'{user.guild.id}']:
        users[f'{user.guild.id}'][f'{user.id}'] = {}
        users[f'{user.guild.id}'][f'{user.id}']['experience'] = 0
        users[f'{user.guild.id}'][f'{user.id}']['level'] = 1
        
    with open('users.json', 'r', encoding = 'utf8')as f:
      users = json.load(f)
    await update_data(users, member)
    with open('users.json', 'w', encoding = 'utf8')as f:
      json.dump(users, f, indent = 4)

  @commands.Cog.listener()
  async def on_message(self, msg):
    async def update_data(users, user):
      if not f'{user.guild.id}' in users:
        users[f'{user.guild.id}'] = {}
      if not f'{user.id}' in users[f'{user.guild.id}']:
        users[f'{user.guild.id}'][f'{user.id}'] = {}
        users[f'{user.guild.id}'][f'{user.id}']['experience'] = 0
        users[f'{user.guild.id}'][f'{user.id}']['level'] = 1
    
    async def add_experience(users, user, exp):
      users[f'{user.guild.id}'][f'{user.id}']['experience'] += exp

    async def level_up(users, user, msg):

      experience = users[f'{user.guild.id}'][f'{user.id}']['experience']
      lvl_start = users[f'{user.guild.id}'][f'{user.id}']['level']
      lvl_end = int(lvl_start+1)
      limit = int(round((10*(lvl_start+1) ** (0.06*lvl_start))+ lvl_start*47))
      if limit <= experience:
        users[f'{user.guild.id}'][f'{user.id}']['experience'] -= experience
        #await msg.author.send(f'{user.mention} 在 {user.guild} 升級了！ 目前等級：{lvl_end}')
        users[f'{user.guild.id}'][f'{user.id}']['level'] = lvl_end
        
    with open('users.json', 'r', encoding = 'utf8')as f:
       users = json.load(f)
    await update_data(users, msg.author)
    await add_experience(users, msg.author, random.randint(1, 15))
    await level_up(users, msg.author, msg)
    with open('users.json', 'w', encoding = 'utf8')as f:
      json.dump(users, f, indent = 4)

  @commands.command()
  async def rank(self,ctx, *, member: discord.Member = None):
    if not member:
      member = ctx.message.author
    with open('users.json', 'r', encoding = 'utf8')as f:
       users = json.load(f)
    level = users[f'{member.guild.id}'][f'{member.id}']['level']
    exp = users[f'{member.guild.id}'][f'{member.id}']['experience']
    limit = round((10*(level+1) ** (0.06*level))+ level*47)
    await ctx.send(f'目前等級：{level} \n目前經驗值：{exp}/{limit}')

async def setup(bot):
  await bot.add_cog(level(bot))