import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
import random
import asyncio

class economy(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    db = sqlite3.connect("main.sqlite")
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS main(
        user_id INTERGER, wallet INTERGER, bank INTERGER
    )''')

  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content == 'ID':
      await msg.channel.send(msg.author.id)

def setup(bot):
  bot.add_cog(economy(bot))