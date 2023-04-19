import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import os
import aiosqlite
import sqlite3

FFMPEG_OPTIONS = {
    'before_options':
    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

import json

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='h^', intents=intents)
bot.remove_command('help')
cogs = [
    "cogs.ordinary", "cogs.voice","cogs.level","cogs.event", "cogs.role", "cogs.ultrasouls"
]


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(
                                  name='h^help',
                                  type=discord.ActivityType.listening))
    print('>> Bot is online ')
    print('>> Loading cogs . . . ')
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(cog + " was loaded.")
        except Exception as e:
            print(e)
    setattr(bot, "db", await aiosqlite.connect('level.db'))
    await asyncio.sleep(3)
    async with bot.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS levels (guild INTEGER, user INTEGER, level INTEGER, xp INTEGER)")


@bot.event
async def on_member_remove(member):
    if member.guild.id == 426975427760881665:
        channel = bot.get_channel(884312764200411157)
        await channel.send(f'{member.mention} 居然拋棄了超古代勇者！')
    elif member.guild.id == 746024720767385720:
        channel = bot.get_channel(851866746930987070)
        await channel.send(f'{member.mention} 已遠離我們而去。')


@bot.event  #未完成
async def on_messaage(message):
    if message.author.bot:
      return
    async with bot.db.cursor() as cursor:
      await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (message.author.id, message.guild.id,))
      xp = await cursor.fetchone()
      await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (message.author.id, message.guild.id,))
      level = await cursor.fetchone()
      if not xp or not level:
        await cursor.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)", (1, 0, message.author.id, message.guild.id,))
        await bot.db.commit()
      xp += random.randint(1,15)
      await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, message.author.id, message.guild.id,))
      if xp >= round((10*(level+1) ** (0.06*level))+ level*47):
        level += 1
        await cursor.execute("UPDATE levels SET xp = 0 AND SET level = ? WHERE user = ? AND guild = ?", (level, message.author.id, message.guild.id,))
        await message.channel.send(f"{message.author.mention} 升到等級 {level} 了！")

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 426974412428804097:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded {extension} done')


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 426974412428804097:
        await bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Un-Loaded {extension} done')


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 426974412428804097:
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Re-Loaded {extension} done')


#日期
import datetime


def gettime():
    x = datetime.datetime.now()
    err = datetime.timedelta(hours=8)
    x += err
    y = x.year
    m = [
        '1 月', '2 月', '3 月', '4 月', '5 月', '6月', '7月', '8月', '9月', '10月',
        '11月', '12月'
    ][x.month - 1]
    d = x.day
    s1 = '日'
    h = x.hour
    mi = x.minute
    s = x.second
    w = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五',
         '星期六'][(x.weekday() + 1) % 7]
    res = '{} {} {} {:02d} {} {:02d}:{:02d}:{:02d}'.format(
        y, w, m, d, s1, h, mi, s)
    return res


import random


def Guess(n):
    tmp = random.randint(1, 10)
    a = ['猜錯了', '猜對了']
    s = f'正解為 {tmp},你的答案為 {n}{a[n == tmp]}'
    return s


@bot.command()
async def guess(ctx, n: int):
    await ctx.send(Guess(n))


@bot.command()
async def now(ctx):
    await ctx.send(gettime())


def EXGuess(n):
    tmp = random.randint(1, 10000)
    a = ['猜錯了', '猜對了']
    s = f'正解為 {tmp},你的答案為 {n}{a[n == tmp]}'
    return s


@bot.command()
async def EXguess(ctx, n: int):
    await ctx.send(EXGuess(n))

#計算機
import math
from math import *


def operation(s):
    s = s.replace(' ', '')
    s = s.replace('^', '**')
    s = s.replace('log', 'log10')
    s = s.replace('ln', 'log')
    i, t = len(s) - 1, 0
    while i >= 0:  # 處理 "factorial 階乘"
        if s[i] == '!':
            if s[i - 1].isdigit():
                t, i = i, i - 1
                while s[i].isdigit():
                    i -= 1
                tmp = s[i + 1:t]
                s = s[:i + 1] + 'factorial(' + tmp + ')' + s[t + 1:]
            else:
                t, right, i = i, 1, i - 2
                while right:
                    if s[i] == ')':
                        right += 1
                    if s[i] == '(':
                        right -= 1
                    i -= 1
                tmp = s[i + 1:t]
                s = s[:i + 1] + 'factorital(' + tmp + ')' + s[t + 1:]
        i -= 1
    try:
        res = round(eval(s), 4)
        return res
    except:
        res = '(太難了算不出來)'
        return res


@bot.command()
async def calc(ctx, *, s):
    ans = operation(s)
    await ctx.send(f'({s}) 答案為 {ans}')

class Invite(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        self.inv = inv
        self.add_item(discord.ui.Button(label = "機器人邀請連結", url = "https://discord.com/api/oauth2/authorize?client_id=830526243437805588&permissions=8&scope=bot"))
    @discord.ui.button(label = "生成邀請連結", style = discord.ButtonStyle.green)
    async def inviteBtn(self, interaction: discord.Interaction, button  = discord.ui.Button):
        await interaction.response.send_message(self.inv, ephemeral=True) #ephemeral = 短暫
  
@bot.command()
async def invite(ctx):  #邀請連結指令
    inv = await ctx.channel.create_invite(max_uses=1, max_age = 900)
    await ctx.send("產生的伺服器邀請連結會在15分鐘後自動銷毀，並且只能使用一次，右邊則是這台機器人的邀請連結", view = Invite(str(inv)))

@bot.command()
async def help(ctx):
    with open('setting.json', 'r', encoding='utf8') as jFile:
        jdata = json.load(jFile)
        embed = discord.Embed(color=0x86ff00)
        #embed.set_author(name = jdata['FORM'])
        embed.set_thumbnail(url=jdata['STICKER'])
        embed.add_field(name='h^help', value='可以看到現在的幫助選單', inline=False)
        embed.add_field(name='h^ping', value='可以看機器人的延遲', inline=False)
        embed.add_field(name='h^now', value='可以得到目前時間', inline=False)
        embed.add_field(name='h^guess (數字)',
                        value='可以試手氣，看你猜不猜得到機器人所想的數字，數字範圍為1~10',
                        inline=False)
        embed.add_field(
            name='h^EXguess (數字)',
            value='給運氣逆天的傢伙玩的，看你猜不猜得到機器人所想的數字，數字範圍為1~10000，猜中拍照給我，我會給你運氣大佬的身份組',
            inline=False)
        embed.add_field(name='h^calc',
                        value='就是計算機，可以算到很大位數的計算機，但是太難的算式或是答案超過2000位數的沒辦法算出來',
                        inline=False)
        embed.add_field(name='h^invite',
                        value='沒錯這個指令升級了，現在用這個指令會出現兩個按鈕，左邊是生成你現在這個伺服器的15分鐘一次性邀請連結，右邊的按鈕則是這個機器人的連結',
                        inline=False)
        embed.add_field(name='h^avatar（成員）',
                        value='可以讓你取得成員的頭貼，然後這其實只是為了寫別的功能誕生出來的附屬品',
                        inline=False)
        embed.add_field(name='h^addrole（身份組名稱）',
                        value='可以讓你獲得一些沒有取得限制的身份組，有哪些想要的身份組歡迎自由輸入指令領取',
                        inline=False)
        embed.add_field(name='---------------------------------------',
                        value='此機器人目前為半成品，極有可能出現問題，請斟酌使用',
                        inline=False)
        embed.add_field(name='請注意，機器人的任何言論皆不代表客家猴立場',
                        value='(雖說這版本應該不需要這句話)',
                        inline=False)
        await ctx.send(embed=embed)

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)
    bot.run(jdata['TOKEN'])
